---
type: item
source-type: "Remaster"
level: "9"
traits: ["[[Disarm]]", "[[Magical]]", "[[Sweep]]", "[[Trip]]"]
price: "{'gp': 700}"
usage: "held-in-two-hands"
bulk: "2"
source: "Pathfinder Howl of the Wild"
---
### `= this.file.name`
**Item** `= this.level`
`= choice(this.traits != null and length(this.traits) > 0, join(this.traits, " "), "")`

`= choice(this.price != null and this.price != "", "**Price** " + this.price, "") + choice(this.usage != null and this.usage != "", choice(this.price != null and this.price != "", "; ", "") + "**Usage** " + this.usage, "") + choice(this.bulk != null and this.bulk != "", choice(this.price != null and this.price != "" or this.usage != null and this.usage != "", "; ", "") + "**Bulk** " + this.bulk, "")`
`= choice(this.activate != null and this.activate != "", "**Activate** " + this.activate, "")`

The three spiked heads of this *+1 striking war flail* are fashioned to resemble the heads of a chimera. Preserved fragments of bone from the creature are fused with the metal of each head, replacing the typical weight at the end of the chain. Each head has been shrunk and preserved for use. You can have only one head slotted at a time and can use only the ability of the currently slotted head, while the other two hang off the pommel. Switching between heads requires an Interact action.

**Dragon** This head does piercing damage instead of the normal bludgeoning damage, plus 1 damage type based on the magical tradition of the chimera's dragon head. (**Arcane** force; **Divine** spirit; **Occult** mental; **Primal** acid, cold, electricity, fire, sonic, or poison, chosen at item creation)

**Activate—Bursting Breath** `pf2:1` (concentrate)

**Frequency** once per 10 minutes

**Requirements** your last action was a successful Strike

**Effect** You tap into the residual energy of the dragon head and release it as a small breath explosion. This does 2d6 untyped damage of the dragon's additional damage type in a @Template[burst|distance:10] centered around one corner of the space the target occupies. After using this, the dragon head attachment loses its additional damage type. You can spend 10 minutes to rest and recharge the head.

**Lion** This head does piercing damage instead of the normal bludgeoning damage, plus 1 additional precision damage if the target is [[Off Guard]].

**Activate—Pouncing Whirl** `pf2:2` (concentrate)

**Frequency** once per 10 minutes

**Requirements** you have not made an attack this turn

**Effect** You tap into the predator speed of a lion. You Stride up to half your Speed and make a Strike against a target. If that creature is within reach of an ally, regardless if they would normally provide flanking or not, that creature is considered off-guard to your Strike. Your additional precision damage against an off-guard creature increases to 1d4. After using this, the lion head loses its additional precision damage. You can spend 10 minutes to rest and recharge the head.

**Goat** If your last action was to Stride at least half your Speed, this does an additional 1d4 force damage.

**Activate—Charging Horns** `pf2:3` (concentrate)

**Frequency** once per 10 minutes

**Effect** You swing the hammer around with the full force of a charging ram. Make a Strike against up to three enemies within your reach. The first two Strikes are at your current attack bonus, and the third is with the normal attack penalty. On a successful hit, the target takes an additional 1d6 force damage and is pushed back 5 feet, or 10 feet on a critical hit. After using this, the goat head loses its additional force damage. You can spend 10 minutes to rest and recharge the head.

**Craft Requirements** The initial raw materials must include all three heads from a chimera.

**Source:** `= this.source` (`= this.source-type`)
