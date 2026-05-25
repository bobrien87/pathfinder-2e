---
type: item
source-type: "Remaster"
level: "17"
traits: ["[[Magical]]", "[[Spellheart]]"]
price: "{'gp': 14000}"
usage: "affixed-to-armor-or-a-weapon"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The golden religious symbol on the top of this spherical incense holder shifts its form to match the faith of its bearer. You gain no benefit from a judgment thurible if you don't worship a deity. The spell DC of any spell cast by activating this item is 35.

- **Armor** After you cast a spell by activating the thurible, the thurible casts 3rd-rank [[Protection]] on you, with a duration of 1 round.
- **Weapon** After you cast a spell by activating the thurible, the weapon gains a rune that lasts until the end of your next turn. It gains the [[Holy]] rune if your deity allows holy sanctification or the [[Unholy]] rune if your deity allows unholy sanctification. If your deity allows both, you can choose which rune the weapon gains. If your deity allows neither, your weapon doesn't gain a rune. The extra damage from this rune is 2d6.

**Activate** Cast a Spell

**Effect** You cast [[Divine Lance]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast 6th-rank [[Divine Wrath]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast [[Divine Decree]]

**Source:** `= this.source` (`= this.source-type`)
