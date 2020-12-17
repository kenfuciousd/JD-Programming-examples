#To install the packages, copy, paste and execute the following command into the bottom left Console window.
install.packages("shiny")
install.packages("leaflet")

#Paste the following code into a new R edit window in RStudio:
library(shiny)
library(leaflet)

r_colors <- rgb(t(col2rgb(colors()) / 255))
names(r_colors) <- colors()

ui <- fluidPage(
  leafletOutput("mymap"),
  p(),
  actionButton("recalc", "New points"),
  p(),
  textOutput("coordinates")
)

server <- function(input, output, session) {
  points <- eventReactive(input$recalc, {
    points = cbind(rnorm(40) * 2 + 13, rnorm(40) + 48)
    output$coordinates <- renderText({ 
      points
    })
    return(points)}, ignoreNULL = FALSE)
  
  observeEvent(input$Map_shape_click, { # update the location selectInput on map clicks
    output$coordinates <- renderText({ 
      "You have selected this"
    })
  })
  output$mymap <- renderLeaflet({
    leaflet() %>%
      addProviderTiles(providers$Stamen.TonerLite,
                       options = providerTileOptions(noWrap = TRUE)
      ) %>%
      addMarkers(data = points())
  })
  
}

shinyApp(ui, server)