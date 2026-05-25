---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Auditory]]", "[[Consumable]]", "[[Magical]]", "[[Visual]]"]
price: "{'gp': 235}"
usage: "held-in-two-hands"
bulk: "L"
source: "Pathfinder Treasure Vault (Remastered)"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

**Activate** `pf2:2` (concentrate, manipulate)

Plucking a talespinner's lyre while focusing on an event you witnessed causes the instrument to create an illusion in a @Template[emanation|distance:50] that plays out your memory of the event in real time, complete with sights, sounds, and smells. You can Sustain the Activation for up to 1 minute to keep it playing. The scene reproduces only what's in its area, including nothing beyond that even if present in the memory. The scene is realistic, but all observers can clearly tell it's an illusion. Observers can't interact with the scene directly nor can they taste or touch elements of it to get a sensation you didn't personally experience, but they can attempt skill checks to discern more about the scene without altering its contents. For example, no one could see something you didn't, such as the true form of a creature polymorphed into a squirrel, but an observer might be able to use Perception and [[Sense Motive]] to discern the squirrel was acting unlike a squirrel should. Once the magic is used, the lyre remains as a non-magical virtuoso instrument.

**Source:** `= this.source` (`= this.source-type`)
