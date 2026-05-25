---
type: item
source-type: "Remaster"
level: "3"
traits: ["[[Magical]]", "[[Spellheart]]"]
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

This dry clay ball becomes malleable when activated, shifting into a variety of forms. The spell attack roll of any spell cast by Activating this item is +7 and the spell DC 17.

- **Armor** You gain resistance 2 to precision damage and a +1 item bonus to saving throws against effects with the morph or polymorph traits.
- **Weapon** After you cast a morph or polymorph spell by activating the *clay sphere*, the weapon becomes malleable, shifting its form to your whims. Your Strikes with the affixed weapon have the versatile bludgeoning, versatile piercing, and versatile slashing trait for 1 minute. Until the end of your next turn, Strikes with the affixed weapon have their damage dice increase by one step.

> [!danger] Effect: Clay Sphere   Armor

> [!danger] Effect: Clay Sphere   Weapon

**Activate** Cast a Spell

**Effect** You cast [[Gouging Claw]].

**Source:** `= this.source` (`= this.source-type`)
