---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 310}"
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

This spherical piece of silvery stone helps you ignore minor issues. You can ignore status penalties to skill checks from [[Clumsy]] 1, [[Enfeebled]] 1, [[Frightened]] 1, [[Sickened]] 1, and [[Stupefied 1]] conditions as long as the value of that condition is 1.

Its resonant power allows you to cast [[Guidance]] as an occult innate cantrip.

**Source:** `= this.source` (`= this.source-type`)
