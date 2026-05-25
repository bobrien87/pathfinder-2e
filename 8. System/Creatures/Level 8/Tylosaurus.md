---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Tylosaurus"
level: "8"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Gargantuan"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+18; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +16, Stealth +19"
abilityMods: ["+7", "+5", "+5", "-4", "+4", "-2"]
abilities_top:
  - name: "Deep Breath"
    desc: "A tylosaurus can hold its breath for 2 hours."
armorclass:
  - name: AC
    desc: "27; **Fort** +17, **Ref** +19, **Will** +14"
health:
  - name: HP
    desc: "137"
abilities_mid:
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +20 (`pf2:1`) (unarmed), **Damage** 2d12+10 piercing plus [[Improved Grab]]"
  - name: "Melee strike"
    desc: "Tail +18 (`pf2:1`), **Damage** 2d6+10 bludgeoning"
spellcasting: []
abilities_bot:
  - name: "Aquatic Drag"
    desc: "`pf2:1` **Requirements** The tylosaurus has a creature [[Grabbed]] <br>  <br> **Effect** The tylosaurus Swims up to half its Speed, carrying the grabbed creature with it."
  - name: "Swallow Whole"
    desc: "`pf2:1` Large, @Damage[(2d6+5)[bludgeoning]], Rupture 18 <br>  <br> The monster attempts to swallow a creature of the listed size or smaller that it has grabbed or restrained in its jaws or mouth. If a swallowed creature is of the maximum size listed, the monster can't use Swallow Whole again. If the creature is smaller than the maximum, the monster can usually swallow more creatures; the GM determines the maximum. The monster attempts an [[Athletics]] check opposed by the grabbed creature's Reflex DC. If it succeeds, it swallows the creature. The monster's mouth or jaws no longer grab a creature it has swallowed, so the monster is free to use them to Strike or Grab once again. The monster can't attack creatures it has swallowed. <br>  <br> A swallowed creature is [[Grabbed]], is [[Slowed]] 1, and has to hold its breath or start suffocating. The swallowed creature takes the listed amount of damage when first swallowed and at the end of each of its turns while it's swallowed. If the victim [[Escapes]] this ability's grabbed condition, it exits through the monster's mouth. This frees any other creature grabbed in the monster's mouth or jaws. A swallowed creature can attack the monster that has swallowed it, but only with unarmed attacks or with weapons of light Bulk or less. The swallowing creature is [[Off-Guard]] against the attack. If the monster takes piercing or slashing damage equaling or exceeding the listed Rupture value from a single attack or spell, the swallowed creature cuts itself free. A creature that gets free by either Escaping or cutting itself free can immediately breathe and exits the swallowing monster's space. <br>  <br> > [!danger] Effect: Engulf and Swallow Whole <br>  <br> If the monster dies, a swallowed creature can be freed by creatures adjacent to the corpse if they spend a combined total of 3 actions cutting the monster open with a weapon or unarmed attack that deals piercing or slashing damage."
  - name: "Vicious Strafe"
    desc: "`pf2:2` The tylosaurus Swims up to its Speed. It can make one jaws Strike and one tail Strike at any points during its movement, each attacking a different target."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Though large in size-sometimes exceeding 40 feet-tylosauruses have sleek bodies and long, narrow snouts. Few creatures compete with them in their environment, as most other aquatic giants reside in deeper water.

The massive swimming reptiles called mosasaurs thrash their powerful tails to propel them after prey. Four articulated, webbed paddles let them precisely steer their paths, and their hinged jaws-much like a snake's-allow mosasaurs to swallow larger creatures than their size would indicate. A small set of secondary pterygoid jaws in their gullets pull in their meals for more efficient digestion. As air breathers, mosasaurs must stay near the surface of the water, competing for food with whales. This proximity to the surface means they often capsize small boats, feasting on the crew members who fall out.

```statblock
creature: "Tylosaurus"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
