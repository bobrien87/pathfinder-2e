---
type: creature
group: ["Dragon", "Primal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Adamantine Dragon (Young, Spellcaster)"
level: "9"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Dragon"
trait_02: "Primal"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+17; [[Darkvision]], [[Scent]] (imprecise) 60 feet, [[Tremorsense]] (imprecise) 60 feet"
languages: "Common, Draconic, Petran"
skills:
  - name: Skills
    desc: "Acrobatics +17, Athletics +21, Intimidation +18, Nature +17, Survival +19, Mining Lore +16"
abilityMods: ["+6", "+2", "+4", "+1", "+2", "+3"]
abilities_top:
  - name: "Adamantine Body"
    desc: "The dragon's unarmed melee Strikes are adamantine."
  - name: "Rock Tunneler"
    desc: "The dragon can burrow through solid stone at a Speed of 20 feet. They can leave a tunnel if they desire, and they usually don't."
armorclass:
  - name: AC
    desc: "27; **Fort** +21, **Ref** +15, **Will** +17"
health:
  - name: HP
    desc: "140; **Immunities** paralyzed, petrified, sleep"
abilities_mid:
  - name: "+2 Status to All Saves vs. Primal"
    desc: ""
  - name: "Abandon Armor"
    desc: "Once the adamantine dragon is reduced to fewer than half their Hit Points, their resistance is reduced by 10 and they gain a +10 circumstance bonus to their Speeds."
  - name: "Frightful Presence"
    desc: "90 feet. DC 26 [[Will]] save <br>  <br> A creature that first enters the area must attempt a Will save. <br>  <br> Regardless of the result of the saving throw, the creature is temporarily immune to this monster's Frightful Presence for 1 minute. <br> - **Critical Success** The creature is unaffected by the presence. <br> - **Success** The creature is [[Frightened]] 1. <br> - **Failure** The creature is [[Frightened]] 2. <br> - **Critical Failure** The creature is [[Frightened]] 4."
  - name: "Resilient Form"
    desc: "`pf2:r` **Trigger** The dragon is critically hit with a weapon or unarmed attack; <br>  <br> **Effect** The dragon's tough scales ward off deadly attacks. The dragon attempts a DC 17 flat check. On a success, the triggering attack becomes a normal hit."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +21 (`pf2:1`) (magical, reach 10 ft., unarmed), **Damage** 2d12+9 piercing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Claw +21 (`pf2:1`) (agile, magical, unarmed), **Damage** 2d8+9 slashing plus [[Knockdown]]"
  - name: "Melee strike"
    desc: "Tail +19 (`pf2:1`) (magical, reach 15 ft.), **Damage** 2d10+9 bludgeoning"
  - name: "Ranged strike"
    desc: "Rock +19 (`pf2:1`) (brutal, range 90 ft.), **Damage** 2d8+9 bludgeoning"
spellcasting:
  - name: "Primal Prepared Spells"
    desc: "DC 28, attack +21<br>**4th** (2 slots) [[Shape Stone]], [[Unfettered Movement]]<br>**3rd** (3 slots) [[Earthbind]], [[One with Stone]], [[Slow]]<br>**2nd** (3 slots) [[Darkness]], [[Shatter]], [[Water Walk]]<br>**1st** (3 slots) [[Air Bubble]], [[Tailwind]], [[Vanishing Tracks]]<br>**Cantrips** [[Caustic Blast]], [[Detect Magic]], [[Know the Way]], [[Sigil]], [[Tangle Vine]]"
abilities_bot:
  - name: "Avalanche Breath"
    desc: "`pf2:2` The dragon belches a mass of boulders that deals @Damage[8d8[bludgeoning]|options:area-damage] damage in a @Template[cone|distance:30] (DC 28 [[Reflex]] save). <br>  <br> They can't use Avalanche Breath again for 1d4 rounds."
  - name: "Burrowing Pounce"
    desc: "`pf2:3` **Requirements** The dragon is burrowed <br>  <br> **Effect** The dragon Burrows, then Leaps out of the ground, landing at a point within 25 feet. The dragon makes a melee Strike against a creature within reach when they land. If the Strike is a critical hit, the target is knocked [[Prone]]."
  - name: "Swallow Whole"
    desc: "`pf2:1` Medium, @Damage[(2d12+4)[bludgeoning]], Rupture 22 <br>  <br> The monster attempts to swallow a creature of the listed size or smaller that it has grabbed or restrained in its jaws or mouth. If a swallowed creature is of the maximum size listed, the monster can't use Swallow Whole again. If the creature is smaller than the maximum, the monster can usually swallow more creatures; the GM determines the maximum. The monster attempts an [[Athletics]] check opposed by the grabbed creature's Reflex DC. If it succeeds, it swallows the creature. The monster's mouth or jaws no longer grab a creature it has swallowed, so the monster is free to use them to Strike or Grab once again. The monster can't attack creatures it has swallowed. <br>  <br> A swallowed creature is [[Grabbed]], is [[Slowed]] 1, and has to hold its breath or start suffocating. The swallowed creature takes the listed amount of damage when first swallowed and at the end of each of its turns while it's swallowed. If the victim [[Escapes]] this ability's grabbed condition, it exits through the monster's mouth. This frees any other creature grabbed in the monster's mouth or jaws. A swallowed creature can attack the monster that has swallowed it, but only with unarmed attacks or with weapons of light Bulk or less. The swallowing creature is [[Off-Guard]] against the attack. If the monster takes piercing or slashing damage equaling or exceeding the listed Rupture value from a single attack or spell, the swallowed creature cuts itself free. A creature that gets free by either Escaping or cutting itself free can immediately breathe and exits the swallowing monster's space. <br>  <br> > [!danger] Effect: Engulf and Swallow Whole <br>  <br> If the monster dies, a swallowed creature can be freed by creatures adjacent to the corpse if they spend a combined total of 3 actions cutting the monster open with a weapon or unarmed attack that deals piercing or slashing damage."
  - name: "Throw Rock"
    desc: "`pf2:1` The monster picks up a rock within reach or retrieves a stowed rock and throws it, making a ranged Strike."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
  - name: "Knockdown"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Knockdown in its damage entry <br>  <br> **Effect** The monster attempts to `act trip` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

The powerful adamantine dragons are one of several dragons known as skymetal dragons. The innate magic that flows through these dragons causes them to draw particular metals to their bodies like magnets or, in some cases, naturally grow these skymetals on their bodies. Adamantine dragons begin their lives with tough scales that are naturally replaced with thicker and even tougher adamantine plating as they grow older. Adamantine dragons are typically steadfast and loyal. Once they commit to a certain purpose, changing their minds is nigh impossible.

Dragons come in myriad forms, with many having magical abilities or connections to magic. Some dragons draw greater power from magic than others, allowing them to manifest abilities or alter their physiques with prolonged exposure to magic. These dragons become more powerful as they age and strengthen their connections with their magical origins. Scholars debate the classification of these dragons, with some preferring the name magical dragons and others using traditional dragons due to their connection to specific magical traditions. Regardless of their names, these dragons share a number of characteristics: their ability to tap into magical energies, intensified might and cunning as they grow older, and an inclination to hoard vast amounts of treasure and wealth.

Draconic Spellcasters
Each dragon features a sidebar on spellcasting dragons of that type. To make a dragon spellcaster, remove the dragon's Draconic Frenzy and Draconic Momentum abilities, and give them the spells outlined in their sidebar. You can swap out any number of these with other spells, provided you keep the same number of spells for each rank. You might also want to increase the dragon's Intelligence, Wisdom, or Charisma modifier by 1 or 2 to reflect their mastery of magic.

```statblock
creature: "Adamantine Dragon (Young, Spellcaster)"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
