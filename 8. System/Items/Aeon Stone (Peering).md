---
type: item
source-type: "Remaster"
level: "16"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 8500}"
usage: "worn"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Over millennia, these mysterious, intricately cut gemstones have been hoarded by mystics and fanatics hoping to discover their secrets. Despite their myriad forms and functions, these stones are purportedly all fragments of crystal tools used by otherworldly entities to construct the universe in primeval times.

When you invest one of these precisely shaped crystals, the stone orbits your head instead of being worn on your body. You can stow an *aeon stone* with an Interact action, and an orbiting stone can be snatched out of the air with a successful Disarm action against you. A stowed or removed stone remains invested, but its effects are suppressed until you return it to orbit your head again.

There are various types of *aeon stones*, each with a different appearance and magical effect. Each *aeon stone* also gains a resonant power when slotted into a special magical item called a *wayfinder*.

This faintly colored prism catches and transforms light. If the aeon stone is in an area of bright light, shades of purple light provide dim light in a 30-foot radius. In that radius, magical items and effects are tinged with purple, the depth of the color revealing their counteract rank.

The GM also secretly rolls a counteract check against any darkness or illusion effect the light touches. It has a counteract modifier of +25. If the light fails to counteract an effect, it won't try again for 24 hours.

Inside a *wayfinder*, the *aeon stone* cannot catch light. However, its resonant power lets you activate or deactivate the *aeon stone's* light emitting from the *wayfinder* as an Interact action.

**Source:** `= this.source` (`= this.source-type`)
