package com.Aridcinemax21

import com.lagradost.cloudstream3.plugins.CloudstreamPlugin
import com.lagradost.cloudstream3.plugins.Plugin
import android.content.Context

@CloudstreamPlugin
class Aridcinemax21Plugin : Plugin() {
    override fun load(context: Context) {
        // Identity persisten MovieBox disiapkan sebelum request pertama.
        Aridcinemax21Extractor.attachContext(context)

        // Hanya mendaftarkan provider utama
        registerMainAPI(Aridcinemax21())
    }
}
