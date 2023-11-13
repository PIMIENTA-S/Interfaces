package com.example.demo;

import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.scene.Scene;
import javafx.scene.control.*;
import javafx.scene.layout.HBox;
import javafx.stage.Stage;

import java.io.IOException;

public class actividad_4 extends Application {
    @Override
    public void start(Stage stage) throws IOException {
        Label nombre = new Label("Nombre");

        TextField entry = new TextField();

        Button enviar = new Button("Enviar");

        Alert a = new Alert(Alert.AlertType.CONFIRMATION);


        EventHandler<ActionEvent> event1 = new EventHandler<ActionEvent>() {
            @Override
            public void handle(ActionEvent actionEvent) {
                a.setTitle("Dialogo de confirmacion");
                a.setHeaderText(entry.getText());
                a.show();
            }
        };

        enviar.setOnAction(event1);

        HBox hBox = new HBox(20);
        hBox.setPadding(new Insets(10,10,10,10));
        hBox.getChildren().addAll(nombre, entry, enviar);

        Scene scene = new Scene(hBox, 500, 200);

        stage.setScene(scene);
        stage.setTitle("Titulo");
        stage.show();


    }
    public static void main(String[] args) {
        launch(args);
    }
}