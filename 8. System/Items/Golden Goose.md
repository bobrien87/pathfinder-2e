---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Cursed]]", "[[Magical]]", "[[Unholy]]"]
price: "{'value': {}}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This life-sized, hollow, golden goose statuette has an open, fanged mouth and an unsettling aura of hunger. Fiends sometimes present it as a gift to mortals whose greed makes them susceptible to temptation. While the *golden goose* can be used without malice, those who possess such a thing often find its glittering lure erodes their morals over time.

**Activate—Golden Goose** (manipulate)

**Frequency** once per day

**Effect** You feed the goose the warm, still-bloody heart of any sapient, non-unholy creature who died within the past hour. The golden goose's eyes flare red as it chews the heart into pulp. Once the heart is destroyed, the goose lays a golden egg worth 50 gp, or 100 gp if you murdered the creature for no reason other than to feed the goose.

After 12 such eggs are laid, the next time you activate the golden goose, it transmutes your heart to gold. This effect functions as [[Petrify]], with a DC 30 [[Fortitude]] save to resist. If you become [[Petrified]], you turn to solid, transparent stone. Your heart becomes a golden egg worth 100 gp, which can be retrieved only by shattering your body. Whether or not you turn to stone, the golden goose dissipates with a honk into sulfurous smoke.

**Source:** `= this.source` (`= this.source-type`)
