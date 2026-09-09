package com.AridDrakor

import com.lagradost.cloudstream3.plugins.CloudstreamPlugin
import com.lagradost.cloudstream3.plugins.Plugin
import android.content.Context

@CloudstreamPlugin
class AridDrakorPlugin : Plugin() {
    override fun load(context: Context) {
        // Identity persisten MovieBox disiapkan sebelum request pertama.
        AridDrakorExtractor.attachContext(context)

        // Hanya mendaftarkan provider utama
        registerMainAPI(AridDrakor())
    }
}
