---
type: item
source-type: "Remaster"
level: "11"
traits: ["[[Invested]]", "[[Magical]]"]
price: "{'gp': 1200}"
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

A flickering aeon stone contains a drop of orichalcum at its center. It remains slightly out of phase with reality, giving it a translucent appearance.

**Activate—Flicker** `pf2:1`

**Frequency** once per day

**Effect** The flickering aeon stone draws you slightly out of sync with the flow of time, causing you to flicker in and out of existence. You become [[Concealed]] for 1 minute, but you can't use this concealment to Hide or [[Sneak]].

**Activate—Enter Stasis** `pf2:1`

**Frequency** once per day

**Effect** The flickering aeon stone pulls you from the flow of time completely, placing you in temporary stasis while you heal, then returning you to reality at the moment you left. You regain @Damage[(2d10+8)[healing]] Hit Points. If you have the clumsy, drained, enfeebled, or stupefied condition, the value of each of these conditions is reduced by 1.

The resonant power grants you a +1 circumstance bonus to initiative rolls.

**Source:** `= this.source` (`= this.source-type`)
