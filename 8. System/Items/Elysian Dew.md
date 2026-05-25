---
type: item
source-type: "Remaster"
level: "12"
traits: ["[[Consumable]]", "[[Magical]]", "[[Potion]]"]
price: "{'gp': 375}"
usage: "held-in-one-hand"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:1` (manipulate)

When you drink sweet, sky-blue *Elysian dew*, for 1 minute, you gain a 10-foot aura that evokes the vitality of Elysium, causing nearby objects to seem more colorful and plants to stand taller. You and any ally that starts its turn in the emanation gain 5 temporary Hit Points, a +1 item bonus to saving throws, and a +1 item bonus to Acrobatics and Athletics checks until the start of your or the ally's next turn. If you're unholy and drink this potion, it fails to work, and you must succeed at a DC 30 [[Fortitude]] save or the potion renders you [[Drained]] 2.

> [!danger] Effect: Aura: Elysian Dew

**Source:** `= this.source` (`= this.source-type`)
