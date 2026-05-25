---
type: item
source-type: "Remaster"
level: "10"
traits: ["[[Consumable]]", "[[Cursed]]", "[[Magical]]", "[[Unholy]]"]
price: "{'per': 1, 'value': {}}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Dark Archive (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

No thorns are visible on this ruby-red crystal rose, which seems to grant a boon to a loved one, but it draws three beads of blood when first bestowed upon an unwitting recipient. Hags delight in using the rose's curse to ruin young lovers, but it can be found anywhere—even buried innocently in a treasure hoard.

You activate the *rose of loves* lost by giving it to someone toward whom you feel romantic attraction. This item functions only if you feel genuine attraction and desire, and it doesn't function if you know the item's curse. If the target accepts the gift, they must succeed at a DC 27 [[Will]] save or be affected by [[Charm]] with an unlimited duration. Every 24 hours, the victim attempts another Will save to break the spell. If they fail three consecutive Will saves, they become [[Doomed]] 1, as the rose inflicts a lethal wasting disease. This value can't decrease while the curse continues. Instead, it worsens every 3 days the victim fails to break the rose's spell, until the victim either dies or shakes off the curse. A successful saving throw or [[Cleanse Affliction]] (of 4th rank or higher) ends the charm and enables the victim to begin decreasing their doomed value.

**Source:** `= this.source` (`= this.source-type`)
