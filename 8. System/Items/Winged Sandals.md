---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Air]]", "[[Invested]]", "[[Magical]]"]
price: "{'gp': 850}"
usage: "wornshoes"
bulk: "L"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Made from soft leather, with delicate white wings attached near the ankles, these sandals are ensorcelled with powerful air magic.

Whenever you fall while wearing these sandals, they automatically cast [[Gentle Landing]] on you. This benefit can't trigger again for 10 minutes.

**Activate—Awaken Wings** `pf2:2` (air, concentrate)

**Frequency** once per day

**Effect** The wings grow in size and propel you through the air, granting you a fly Speed of 30 feet for 10 minutes.

> [!danger] Effect: Winged Sandals

**Source:** `= this.source` (`= this.source-type`)
