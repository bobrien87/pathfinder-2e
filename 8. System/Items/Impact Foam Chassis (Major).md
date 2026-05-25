---
type: item
source-type: "Remaster"
level: "14"
traits: ["[[Consumable]]", "[[Gadget]]"]
price: "{'gp': 650}"
usage: "worngarment"
bulk: "L"
source: "Pathfinder Guns & Gears"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** see below

While you're wearing an impact foam chassis wrapped around your body, it Activates automatically whenever you fall at least 10 feet, causing a layer of soft, flexible impact foam to expand beneath and around you to cushion the fall. The impact foam decreases the falling damage by up to the listed amount, taking damage equal to the amount of falling damage the foam reduced. If this is enough to destroy the foam, it disperses immediately. However, if the foam has any Hit Points remaining, it remains surrounding you for up to 1 minute.

While you're surrounded in foam, you are [[Immobilized]] and have standard cover against other creatures, and other creatures have standard cover against you. The foam has an [[Escape]] DC of 15; a creature can also remove it by spending three Interact actions. You or others can also attack the foam (the foam has an AC of 12), which disperses if reduced to 0 Hit Points.

A greater impact foam chassis prevents up to 200 falling damage and has 200 Hit Points.

**Source:** `= this.source` (`= this.source-type`)
