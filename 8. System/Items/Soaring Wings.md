---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Invested]]", "[[Magical]]", "[[Tattoo]]"]
price: "{'gp': 750}"
usage: "tattooed-on-the-body"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Wings, normally tattooed on the upper back, enable you to fly when activated. The visual manifestation is typically a slight glow or ripple in the ink, but some artists make it so the tattoo creates a glowing aura or lines of light in the shape of wings.

**Activate** `pf2:2` (concentrate)

**Frequency** once per day

**Effect** For 10 minutes, you gain a fly Speed equal to either your land Speed or 20 feet, whichever is greater.

> [!danger] Effect: Soaring Wings

**Source:** `= this.source` (`= this.source-type`)
