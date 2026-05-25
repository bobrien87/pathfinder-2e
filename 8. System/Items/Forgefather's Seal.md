---
type: item
source-type: "Remaster"
level: "24"
traits: ["[[Artifact]]", "[[Divine]]"]
price: "{'value': {}}"
usage: "etched-onto-armor"
bulk: "—"
source: "Pathfinder GM Core"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

This rune was created by Torag, god of the forge, protection, and strategy, and shared with his greatest artisans and warriors. Torag designed a small number of these seals as gifts to allied good deities; each one is nearly identical but has a different spell effect when using the reaction activation; for instance, Sarenrae's seal casts [[Sunburst]] instead of *earthquake*.

A seal constantly rings with the quiet sound of a hammer striking an anvil when etched onto a *runestone*. A *Forgefather's seal* can be etched only onto armor that can bear two or more property runes, and it is so powerful that it takes the place of two property runes. While wearing armor etched with a *Forgefather's seal*, you gain fire resistance 40. You ignore the armor's check penalty and Speed penalty (if any); if the armor is light or medium, increase its item bonus to AC by 1. In addition, any shield you wield automatically recovers 10 Hit Points at the start of your turn each round.

> [!danger] Effect: Forgefather's Seal

**Activate—Retributive Rebuff** R (manipulate)

**Frequency** once per hour

**Trigger** You are hit by an attack

**Effect** The *Forgefather's seal* glows and your armor shakes as it absorbs the blow. The attack's damage is reduced by 100 and you cast [[Earthquake]] (DC 40), centered directly on the triggering creature. You decide the area of the *earthquake* when you Cast the Spell, from as small as the size of the creature and up to a @Template[burst|distance:60].

**Activate—Seal of Mending** `pf2:3` (manipulate)

**Frequency** once per day

**Effect** You call upon on the restorative powers of the seal to repair an item within reach. The rune instantly restores the item to full Hit Points, even if the item was destroyed, using the effects of the [[Remake]] spell, so long as the majority of the item is available for the repair. The seal can restore even magic items and artifacts of its level or lower. Once you have used this ability, the seal's ability to automatically repair shields becomes inactive until the next time you make your daily preparations.

**Activate—Stalwart Sacrifice** `pf2:f` (concentrate)

**Trigger** You have not acted yet on your turn

**Effect** You call upon Torag to defend your allies and those around you, sacrificing yourself in the process. Creatures of your choosing within 60 feet recover all their Hit Points. If any of the creatures are dead, they are instead brought back to life with half of their maximum Hit Points. The chosen creatures also gain a +4 status bonus to AC and saving throws, and fast healing 15 for 1 hour. You can use this ability to bring back to life a creature that requires a [[Wish]] ritual or divine intervention to raise from the dead, as long as you choose no other creatures within 60 feet to recover. Once you use this activation, you are turned into a perfect statue made from stone or metal that depicts you in a glorious pose honoring your sacrifice, and you can never be restored. The *Forgefather's seal* remains on this statue and can be transferred to another suit of armor or a runestone as normal.

> [!danger] Effect: Forgefather's Seal (Stalwart Sacrifice)

**Destruction** Using the *Forgefather's seal* ability to bring the dead back to life on an evil demigod causes it to shatter in a violent explosion that destroys the seal and the statue made as part of the sacrifice, erasing all knowledge of the user from existence. It does, however, bring the evil demigod back to life.

**Source:** `= this.source` (`= this.source-type`)
