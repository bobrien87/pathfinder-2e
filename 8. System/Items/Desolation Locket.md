---
type: item
source-type: "Remaster"
level: "8"
traits: ["[[Magical]]", "[[Spellheart]]"]
price: "{'gp': 470}"
usage: "affixed-to-armor-or-a-weapon"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The surface of this golden, heart-shaped locket is nearly worn through with cracks. If opened, it reveals a portrait of someone the bearer loved dearly and has lost. The spell DC of any spell cast by activating this item is 24.

- **Armor** The *desolation locket* numbs you to further despair, and you gain a +2 item bonus to saving throws against emotion effects.
- **Weapon** (emotion, mental) After you cast a non-cantrip spell by activating the *locket*, you emanate an aura of hopelessness in a @Template[emanation|distance:5] until the start of your next turn. A creature that ends its turn in the aura must succeed at a DC 24 [[Will]] save saving throw against the locket's spell DC or become [[Slowed]] 1 ([[Slowed]] 2 on a critical failure) until the end of its next turn.

> [!danger] Effect: Desolation Locket   Armor

> [!danger] Effect: Desolation Locket   Weapon

**Activate** Cast a Spell

**Effect** You cast [[Haunting Hymn]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast [[Fear]].

**Source:** `= this.source` (`= this.source-type`)
