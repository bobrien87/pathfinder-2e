---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Magical]]", "[[Poison]]", "[[Spellheart]]"]
price: "{'gp': 55}"
usage: "affixed-to-armor-or-a-weapon"
bulk: "L"
source: "Pathfinder #202: Severed at the Root"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This small piece of wood is finely carved to depict a foxglove. The spell DC of any spell cast by Activating this item is 17.

- **Armor** You gain resistance 2 to poison damage.

- **Weapon** After you cast a plant spell by activating the foxglove token, your Strikes with the weapon it's attached to deal an additional 1d4 poison damage until the end of your next turn.

**Activate** Cast a Spell

**Effect** You cast [[Puff of Poison]].

**Source:** `= this.source` (`= this.source-type`)
