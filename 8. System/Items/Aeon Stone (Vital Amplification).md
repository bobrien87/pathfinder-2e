---
type: item
source-type: "Remaster"
level: "7"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 330}"
usage: "worn"
bulk: "—"
source: "Pathfinder #215: To Blot Out the Sun"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

Aeon stones are magical, intricately cut gemstones that orbit the head of their owners and grant them a magical effect. The ancient Azlanti empire made many advances in aeon stone technology, creating countless new aeon stones and devising innovative methods to use aeon stones to their greatest effect. The first wayfinders—one of many devices in which aeon stones can be slotted to gain additional resonant powers—were created in Azlant.

When you invest one of these precisely shaped crystals, the stone orbits your head instead of being worn on your body. You can stow an aeon stone with an Interact action, and an orbiting stone can be snatched out of the air with a successful [[Disarm]] action against you. A stowed or removed stone remains invested, but its effects are suppressed until you return it to orbit your head again.

There are various types of aeon stones, each with a different appearance, magical effect, and resonant power.

A vital amplification aeon stone improves the flow of vital energy through your body, speeding the healing process and safeguarding your body from life-draining effects. Whenever you regain Hit Points, you regain an additional 1 Hit Point for each 10 Hit Points regained (minimum 1 additional Hit Point). The resonant power grants you resistance 5 to void damage.

**Source:** `= this.source` (`= this.source-type`)
