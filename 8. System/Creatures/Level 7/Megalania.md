---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Megalania"
level: "7"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Huge"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15; [[Low-Light Vision]], [[Scent]] (imprecise) 60 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +18, Stealth +15"
abilityMods: ["+7", "+2", "+4", "-4", "+2", "-2"]
abilities_top:
  - name: "Megalania Venom"
    desc: "**Saving Throw** DC 25 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** 1d6 poison damage and [[Clumsy]] 1 (1 round) <br>  <br> **Stage 2** 2d6 poison damage, [[Clumsy]] 2, and [[Off Guard]] (1 round) <br>  <br> **Stage 3** 2d6 poison damage, [[Clumsy]] 3, and [[Off Guard]] (1 round)"
armorclass:
  - name: AC
    desc: "25; **Fort** +17, **Ref** +15, **Will** +13"
health:
  - name: HP
    desc: "125"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +18 (`pf2:1`) (reach 10 ft., unarmed), **Damage** 2d10+9 piercing plus [[Grab]] plus [[Megalania Venom]]"
spellcasting: []
abilities_bot:
  - name: "Swallow Whole"
    desc: "`pf2:1` Large, @Damage[(2d10+7)[bludgeoning]], Rupture 16 <br>  <br> The monster attempts to swallow a creature of the listed size or smaller that it has grabbed or restrained in its jaws or mouth. If a swallowed creature is of the maximum size listed, the monster can't use Swallow Whole again. If the creature is smaller than the maximum, the monster can usually swallow more creatures; the GM determines the maximum. The monster attempts an [[Athletics]] check opposed by the grabbed creature's Reflex DC. If it succeeds, it swallows the creature. The monster's mouth or jaws no longer grab a creature it has swallowed, so the monster is free to use them to Strike or Grab once again. The monster can't attack creatures it has swallowed. <br>  <br> A swallowed creature is [[Grabbed]], is [[Slowed]] 1, and has to hold its breath or start suffocating. The swallowed creature takes the listed amount of damage when first swallowed and at the end of each of its turns while it's swallowed. If the victim [[Escapes]] this ability's grabbed condition, it exits through the monster's mouth. This frees any other creature grabbed in the monster's mouth or jaws. A swallowed creature can attack the monster that has swallowed it, but only with unarmed attacks or with weapons of light Bulk or less. The swallowing creature is [[Off-Guard]] against the attack. If the monster takes piercing or slashing damage equaling or exceeding the listed Rupture value from a single attack or spell, the swallowed creature cuts itself free. A creature that gets free by either Escaping or cutting itself free can immediately breathe and exits the swallowing monster's space. <br>  <br> > [!danger] Effect: Engulf and Swallow Whole <br>  <br> If the monster dies, a swallowed creature can be freed by creatures adjacent to the corpse if they spend a combined total of 3 actions cutting the monster open with a weapon or unarmed attack that deals piercing or slashing damage."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Megalanias, like their smaller cousins the giant monitor lizards, strike fast and use their powerful bite to grip their prey. They prefer to swallow their prey whole rather than risk others getting a bite of a hard-won meal.

```statblock
creature: "Megalania"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
