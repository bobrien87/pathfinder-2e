---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Platecarpus"
level: "3"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+9; [[Low-Light Vision]], [[Scent]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +9, Stealth +11"
abilityMods: ["+5", "+4", "+3", "-4", "+2", "-2"]
abilities_top:
  - name: "Deep Breath"
    desc: "A platecarpus can hold its breath for 2 hours."
armorclass:
  - name: AC
    desc: "19; **Fort** +10, **Ref** +11, **Will** +7"
health:
  - name: HP
    desc: "46"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +12 (`pf2:1`) (unarmed), **Damage** 1d12+5 piercing plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Aquatic Drag"
    desc: "`pf2:1` **Requirements** The platecarpus has a creature [[Grabbed]] <br>  <br> **Effect** The platecarpus Swims up to half its Speed, carrying the grabbed creature with it."
  - name: "Strafing Chomp"
    desc: "`pf2:1` The platecarpus Swims up to its Speed, making one jaws Strike at any point along the way. The Strike deals half damage."
  - name: "Swallow Whole"
    desc: "`pf2:1` Medium, @Damage[(1d6+2)[bludgeoning]], Rupture 10 <br>  <br> The monster attempts to swallow a creature of the listed size or smaller that it has grabbed or restrained in its jaws or mouth. If a swallowed creature is of the maximum size listed, the monster can't use Swallow Whole again. If the creature is smaller than the maximum, the monster can usually swallow more creatures; the GM determines the maximum. The monster attempts an [[Athletics]] check opposed by the grabbed creature's Reflex DC. If it succeeds, it swallows the creature. The monster's mouth or jaws no longer grab a creature it has swallowed, so the monster is free to use them to Strike or Grab once again. The monster can't attack creatures it has swallowed. <br>  <br> A swallowed creature is [[Grabbed]], is [[Slowed]] 1, and has to hold its breath or start suffocating. The swallowed creature takes the listed amount of damage when first swallowed and at the end of each of its turns while it's swallowed. If the victim [[Escapes]] this ability's grabbed condition, it exits through the monster's mouth. This frees any other creature grabbed in the monster's mouth or jaws. A swallowed creature can attack the monster that has swallowed it, but only with unarmed attacks or with weapons of light Bulk or less. The swallowing creature is [[Off-Guard]] against the attack. If the monster takes piercing or slashing damage equaling or exceeding the listed Rupture value from a single attack or spell, the swallowed creature cuts itself free. A creature that gets free by either Escaping or cutting itself free can immediately breathe and exits the swallowing monster's space. <br>  <br> > [!danger] Effect: Engulf and Swallow Whole <br>  <br> If the monster dies, a swallowed creature can be freed by creatures adjacent to the corpse if they spend a combined total of 3 actions cutting the monster open with a weapon or unarmed attack that deals piercing or slashing damage."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

The mid-sized platecarpuses are the most common type of mosasaur. They're typically 15 feet long, but larger specimens can grow up to 20 feet. The larger varieties sometimes eat Medium humanoids, but most stick to smaller fare.

The massive swimming reptiles called mosasaurs thrash their powerful tails to propel them after prey. Four articulated, webbed paddles let them precisely steer their paths, and their hinged jaws-much like a snake's-allow mosasaurs to swallow larger creatures than their size would indicate. A small set of secondary pterygoid jaws in their gullets pull in their meals for more efficient digestion. As air breathers, mosasaurs must stay near the surface of the water, competing for food with whales. This proximity to the surface means they often capsize small boats, feasting on the crew members who fall out.

```statblock
creature: "Platecarpus"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
