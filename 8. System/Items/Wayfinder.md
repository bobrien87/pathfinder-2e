---
type: item
source-type: "Remaster"
level: "2"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 28}"
usage: "worn"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Access** member of the Pathfinder Society

This compact compass repurposes ancient technology to draw fantastic powers from the mysterious magical items called *aeon stones*. It serves as a badge of office for agents of the Pathfinder Society and as a status symbol among adventurers of any stripe. A *wayfinder* functions as a compass.

An indentation in the middle of the *wayfinder* can hold a single *aeon stone*. Placing an *aeon stone* in this indentation provides you all the benefits of having the *aeon stone* orbiting your head, but it protects the stone from being noticed or stolen as easily. You invest a *wayfinder* and the *aeon stone* within it simultaneously, and they count as only one item toward your investiture limit. An invested *aeon stone* slotted in a *wayfinder* also grants its resonant power.

If you have more than one *wayfinder* with an invested *aeon stone* on your person at a given time, destructive interference from their resonance prevents you from gaining benefits from any of them. You can still benefit from additional *aeon stones* orbiting your head, just not in *wayfinders*.

**Activate—Light** A (concentrate)

**Effect** The *wayfinder* is targeted by a 1st-rank [[Light]] spell.

**Source:** `= this.source` (`= this.source-type`)
