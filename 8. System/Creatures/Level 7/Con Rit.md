---
type: creature
group: ["Animal", "Aquatic"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Con Rit"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Animal"
trait_02: "Aquatic"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15; [[Darkvision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +13, Athletics +18, Stealth +13"
abilityMods: ["+6", "+3", "+4", "-5", "+1", "-4"]
abilities_top:
  - name: "Con Rit Venom"
    desc: "**Saving Throw** DC 25 [[Fortitude]] save; <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d10 poison (1 round) <br>  <br> **Stage 2** 2d10 poison and [[Off Guard]] (1 round); <br>  <br> **Stage 3** 2d10 poison, off-guard, and [[Slowed]] 1 (1 round)"
armorclass:
  - name: AC
    desc: "27; **Fort** +17, **Ref** +14, **Will** +10"
health:
  - name: HP
    desc: "100; **Weaknesses** bludgeoning 5; **Resistances** slashing 5, piercing 5"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Mandible +18 (`pf2:1`) (reach 15 ft.), **Damage** 2d10+8 piercing plus [[Con Rit Venom]]"
spellcasting: []
abilities_bot:
  - name: "Spit Venom"
    desc: "`pf2:2` The con rit spits a propulsive blast of venom that deals @Damage[2d10[poison],2d10[bludgeoning]|options:area-damage] damage in a @Template[line|distance:30] (DC 25 [[Fortitude]] save). Creatures who fail their save are also pushed 10 feet. <br>  <br> The con rit cannot use Spit Venom again for 1d4 rounds."
  - name: "Undulate"
    desc: "`pf2:1` The con rit Swims. During this movement, it can pass through spaces as narrow as 5 feet without Squeezing."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The con rit is a hulking aquatic centipede that has traded its hundreds of legs for just as many fins. This sea insect swims with a grace that is just as majestic as it is unnerving. The con rit is dark brown on its dorsal side and sickly yellow on its ventral surface. This makes it much more difficult to spot, whether looking from above or below. Its exoskeleton is as hard as iron, and the shifting of its plates makes an elongated, eerie ringing sound as it swims.

Many once thought the con rit to be a dragon of some kind. This was due not only to its massive size but also to its ability to launch its venom in a concentrated blast. It would use this technique to shoot birds out of the sky or knock sailors off ships. Their movement through the water is also not entirely dissimilar to that of dragons. Those who seek out a con rit's lair in search of treasure are usually disappointed (when they aren't eaten alive by the huge insect).

There are legends that a con rit, much like a phoenix, is reborn after its death. This, however, is not the case. A con rit will make a nest far below the surface of its territory, usually in underwater caves. Throughout its life, a con rit will lay thousands of eggs in its cave that will never hatch. The con rit will eat any egg that gets too old, but there are always large numbers of them remaining. When a con rit dies, it releases a strong-smelling chemical into the air and water that triggers the hatching process. The eggs will slowly crack open within the month, and hundreds of baby con rits will begin to fight each other for territory. By year's end, one will win and reach full maturity. This cycle is what has led to the legends of endless rebirth. Other stories say that every generation of the con rit is ever so slightly smaller, leading to tales of ancient con rits that were hundreds of feet long. However, the size of such legendary insects has yet to be confirmed by scholars who study such things.

```statblock
creature: "Con Rit"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
