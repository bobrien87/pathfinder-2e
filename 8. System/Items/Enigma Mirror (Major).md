---
type: item
source-type: "Remaster"
level: "13"
traits: ["[[Magical]]", "[[Spellheart]]"]
price: "{'gp': 2750}"
usage: "affixed-to-armor-or-a-weapon"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Mist fills the glass of this small circular hand mirror, creating strange patterns in the shifting gray wisps. The back of the mirror bears a flowing script engraving in an unknown language. The spell DC of any spell cast by activating this item is 30.

- **Armor** After you cast an illusion spell by activating the mirror, choose one ally within 30 feet. That ally is [[Concealed]] as if seen in a misty mirror, until the end of your next turn.
- **Weapon** After you cast an illusion spell by activating the mirror, illusory copies of the weapon swirl in the air around it. You're affected by the [[Thicket of Knives]] spell until the end of your next turn. The spell ends if you stop wielding the affixed weapon.

**Activate** Cast a Spell

**Effect** You cast [[Forbidding Ward]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast [[Mirror's Misfortune]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast [[Mirror Malefactors]].

**Source:** `= this.source` (`= this.source-type`)
