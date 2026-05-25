---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Catalyst]]", "[[Consumable]]", "[[Magical]]"]
price: "{'gp': 150}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** Cast a Spell (add 1 action)

The thorny growths on a rosethorn ram's horns break off into jagged pieces when these animals fight. When used to enhance the two-action version of a [[Howling Blizzard]] spell, these thorns cause the squares directly adjacent to every creature within the spell's area of effect to become littered with icy caltrops. The first creature that moves into each affected square must succeed at an [[Acrobatics]] check with a DC equal to spell's save DC or take an amount of cold damage equal to the spell's rank. When a creature takes damage from the icy caltrops, enough are damaged that other creatures moving into that square are safe.

**Source:** `= this.source` (`= this.source-type`)
