package com.example.secondApp;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;
import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Button buttonStartRitual = findViewById(R.id.buttonStartRitual);
        Button buttonDiagnose = findViewById(R.id.buttonDiagnose);
        Button buttonGratitudeLog = findViewById(R.id.buttonGratitudeLog);

        buttonStartRitual.setOnClickListener(v ->
                Toast.makeText(this, "🌼 Welcome is updated", Toast.LENGTH_SHORT).show());

        buttonDiagnose.setOnClickListener(v ->
                Toast.makeText(this, "🔧 Running diagnostics...", Toast.LENGTH_SHORT).show());

        buttonGratitudeLog.setOnClickListener(v ->
                Toast.makeText(this, "📜 Logging gratitude", Toast.LENGTH_SHORT).show());
