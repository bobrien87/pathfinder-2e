---
type: creature
group: ["Beast"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Hodag"
level: "6"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Beast"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+14; [[Darkvision]], [[Scent]] (imprecise) 30 feet"
languages: "Common (Can't speak any language)"
skills:
  - name: Skills
    desc: "Athletics +13, Stealth +14, Survival +12"
abilityMods: ["+5", "+4", "+5", "-2", "+4", "+0"]
abilities_top:
  - name: "Trackless"
    desc: "A hodag sweeps the ground behind it with its tail as it moves, obscuring its tracks. The DCs of checks to [[Track]] a hodag are increased by 10."
armorclass:
  - name: AC
    desc: "24; **Fort** +17, **Ref** +14, **Will** +12"
health:
  - name: HP
    desc: "90"
abilities_mid:
  - name: "Ferocity"
    desc: "`pf2:r` **Trigger** The monster is reduced to 0 HP. <br>  <br> **Effect** The monster avoids being knocked out and remains at 1 HP, but its [[Wounded]] value increases by 1. When it is Wounded 3, it can no longer use this ability"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +17 (`pf2:1`), **Damage** 2d8+8 piercing"
  - name: "Melee strike"
    desc: "Claw +17 (`pf2:1`) (agile), **Damage** 2d6+8 slashing"
  - name: "Melee strike"
    desc: "Spiked Tail +17 (`pf2:1`) (reach 10 ft., versatile p), **Damage** 2d6+8 bludgeoning plus [[Knockdown]]"
spellcasting: []
abilities_bot:
  - name: "Rip and Tear"
    desc: "`pf2:2` The hodag makes two claw Strikes and one jaws Strike in any order."
  - name: "Toss"
    desc: "`pf2:2` The hodag Strides, then makes a Strike against a target in reach. If it moves at least 20 feet and succeeds at its Strike, the hodag deals damage normally and then attempts an Athletics check against the creature's Fortitude DC to toss the enemy into the air. On a success, the tossed creature is thrown 10 feet in a straight line in the direction of the hodag's choice and then lands [[Prone]]. <br>  <br> If the creature is knocked into a solid object, it takes 1d6 bludgeoning damage before landing prone. The hodag can instead toss a creature straight up in the air. The creature lands in the same square where it started, takes 1d6 bludgeoning damage, and falls prone."
  - name: "Knockdown"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Knockdown in its damage entry <br>  <br> **Effect** The monster attempts to `act trip` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Because they're often fantastically described in the wild tall tales of loggers or miners, hodags are considered by many to exist only in local folklore. However, some individuals have actually encountered these dangerous beasts firsthand, though even fewer have lived to tell the tale.

Hodags are reptilian creatures the size of bulls. Their vicious claws can tear creatures apart in seconds. Their backs sport dozens of long spines, running from their snouts all the way down the length of their powerful tails. Their wide mouths are full of sharp, twisted rows of teeth, not unlike those of a shark. The hodags' rough, scaly hides carry hues of green and brown, allowing them to blend into their forest surroundings where they ambush prey. Only their glowing red eyes reveal their presence, though hodags have learned to use this to their advantage by drawing attention to their eyes in one area, closing them, and stealthily moving to another area to discombobulate prey.

Because hodags are rarely seen, their biology is a matter of some mystery. While they may have evolved as natural beasts, rumors persist that they spring from curses or as punishment for mistreating livestock.

In the wintertime, when snow and ice blanket a region, hodags grow a foul-smelling coat of greasy, dark-brown fur that sprouts in tufts from between their scales. A typical hodag measures over 10 feet long from snout to tail and weighs upward of 700 pounds.

```statblock
creature: "Hodag"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
