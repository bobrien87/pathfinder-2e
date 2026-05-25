---
type: item
source-type: "Remaster"
level: "6"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 225}"
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

Once holy relics, the creation of crescent aeon stones was inspired by Acavna, goddess of the moon and protection. The crescent aeon stone continually sheds dim light in a 5-foot radius.

**Activate—Moonbeam** `pf2:2` (concentrate, divine, holy, light, spirit)

**Frequency** once per day

**Effect** The crescent aeon stone fires a blast of silvery moonlight in a @Template[type:line|distance:100], dealing 4d12 spirit damage to all creatures in the area (DC 22 [[Reflex]] save). This is silver damage for the purposes of weaknesses, resistances, and the like.

The resonant power enables you to cast forbidding ward as a divine innate cantrip.

**Source:** `= this.source` (`= this.source-type`)
