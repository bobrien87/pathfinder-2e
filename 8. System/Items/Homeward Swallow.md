---
type: item
source-type: "Remaster"
level: "5"
traits: ["[[Invested]]", "[[Magical]]", "[[Tattoo]]"]
price: "{'gp': 150}"
usage: "tattooed-on-the-body"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This small tattoo of a swallow always points toward your home. The tattooing must take place at a location you consider to be your home, or the magic fails to bind with the ink. When you travel to your home using teleportation that can be off target, such as [[Teleport]] or [[Interplanar Teleport]], you arrive exactly at your home. If your home is destroyed or you come to believe a new place is your home, this tattoo fades from your skin.

**Activate** `pf2:1` (concentrate)

**Effect** You sense the direction toward your home.

**Source:** `= this.source` (`= this.source-type`)
