---
type: item
source-type: "Remaster"
level: "4"
traits: ["[[Adjustment]]", "[[Mechanical]]"]
price: "{'gp': 100}"
usage: "affixed-to-armor"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

These small, metallic devices resemble squashed spheres. They each contain a tiny gyroscope that's incredibly sensitive to vibrations in the earth. While typically worn on one's footwear, the device can be affixed to any part of your armor.

**Activate** `pf2:f` (manipulate)

**Frequency** once per day

**Effect** You stomp a foot, clap your hands, or create some other source of sound, gaining tremorsense as an imprecise sense with a range of 20 feet for the next 10 minutes.

> [!danger] Effect: Tremorsensors

**Source:** `= this.source` (`= this.source-type`)
