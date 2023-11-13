package com.example.demo;

import javafx.application.Application;
import javafx.event.EventHandler;
import javafx.scene.Scene;
import javafx.scene.control.Label;
import javafx.scene.input.MouseEvent;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.stage.Stage;

import java.io.IOException;

public class actividad_3 extends Application {
    @Override
    public void start(Stage stage) throws IOException {

        Label texto = new Label("Eventos del raton");
        texto.setFont(new Font(20));

        EventHandler<MouseEvent> mouseHandler = new EventHandler<MouseEvent>() {
            @Override
            public void handle(MouseEvent mouseEvent) {
                texto.setText("Lo clickeo");
                texto.setFont(new Font(20));
                texto.setTextFill(Color.RED);
            }
        };

        texto.setOnMouseClicked(mouseHandler);


        VBox root = new VBox(10);
        root.getChildren().add(texto);
        Scene scene = new Scene(root, 300, 250);
        stage.setScene(scene);
        stage.show();


    }

    public static void main(String[] args) {
        launch(args);
    }
}