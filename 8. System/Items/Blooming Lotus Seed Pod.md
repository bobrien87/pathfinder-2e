---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Consumable]]", "[[Magical]]", "[[Plant]]", "[[Wood]]"]
price: "{'gp': 68}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Rage of Elements"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The seeds of this lotus seed pod scatter with incredible ease and accuracy, quickly growing into temporary plants.

**Activate - Floating Pads** `pf2:1` (manipulate)

**Effect** You scatter the blooming lotus seed pod's seeds across a non-damaging liquid surface within 40 feet of you, where they form into 5 lotus pads that each float in place in a separate square within range for 1 minute. Each lotus pad has a 10- foot radius and can support 1 Large creature, 2 Medium creatures, or 4 Small creatures.

**Activate - Blooming Flower** 10 minutes (manipulate)

**Effect** You plant the blooming lotus seed pod in the ground and a giant lotus flower blooms in that square. Over the next 8 hours, creatures who sleep for at least 6 hours within 30 feet of the lotus flower gain the benefits of long-term rest as though they'd spent an entire day and night resting, and all creatures within the affected area are immune to the effects of the [[Nightmare]] spell and other magical effects that affect only sleeping creatures.

**Source:** `= this.source` (`= this.source-type`)
