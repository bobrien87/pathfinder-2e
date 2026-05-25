---
type: item
source-type: "Remaster"
level: "15"
traits: ["[[Magical]]", "[[Spellheart]]"]
price: "{'gp': 6500}"
usage: "affixed-to-armor-or-a-weapon"
bulk: "—"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This jagged, bony growth narrows to a sharp, pointed tip. Deep groves from some former battle scar its surface. The bearer of a *saurian spike* often feels a sudden surge in power and confidence. The spell attack modifier of any spell cast by activating this item is +24.

- **Armor** You gain precise scent with a range of 60 feet.
- **Weapon** (auditory, emotion, fear, visual) When you cast a polymorph spell by activating the spike, your battle form is exceptionally fearsome. Each enemy in a @Template[emanation|distance:60] must succeed at a DC 34 [[Will]] save saving throw or become [[Frightened]] 2 ([[Frightened]] 3 on a critical failure).

> [!danger] Effect: Saurian Spike   Armor

**Activate** Cast a Spell

**Effect** You cast [[Gouging Claw]].

**Activate** Cast a Spell

**Frequency** once per day

**Effect** You cast 7th-rank [[Dinosaur Form]].

**Source:** `= this.source` (`= this.source-type`)
