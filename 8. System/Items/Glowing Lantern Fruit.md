---
type: item
source-type: "Remaster"
level: "1"
traits: ["[[Consumable]]", "[[Magical]]", "[[Wood]]"]
price: "{'gp': 4}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The flesh of this fruit pod resembles a stylized paper lantern, with a woody, geometric structure and thin layers of flesh, complete with a glow coming from the interior.

**Activate - Lantern Light** `pf2:1` (manipulate)

**Effect** The *glowing lantern fruit* sheds bright light in a 60-foot radius (and dim light for the next 60 feet) for 8 hours. While the light is shining, you can Interact with the *glowing lantern fruit* to open or close some of its reflective leaves, making the light directional like a bull's-eye lantern or a hooded lantern.

> [!danger] Effect: Glowing Lantern Fruit (Lantern Light)

**Activate - Fire Fruit** 10 minutes (manipulate)

**Effect** You plant the *glowing lantern fruit* in the ground upside down. The petals of the lantern peel away, while the fruit inside glows hotter. For the next 8 hours, the *glowing lantern fruit* emits as much light and heat as a bonfire, giving all creatures within 15 feet immunity to the effects of mild and severe cold temperatures for as long as they're within the area.

**Source:** `= this.source` (`= this.source-type`)
