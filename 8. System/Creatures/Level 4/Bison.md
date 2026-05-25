---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Bison"
level: "4"
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
    desc: "+8; [[Scent]] (imprecise) 60 feet"
languages: ""
skills:
  - name: Skills
    desc: "Athletics +14, Survival +10"
abilityMods: ["+6", "+3", "+5", "-5", "+2", "-1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "20; **Fort** +13, **Ref** +11, **Will** +8"
health:
  - name: HP
    desc: "70"
abilities_mid:
  - name: "Cold Adaptation"
    desc: "The bison reduces the effects it suffers from cold environments by one step."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Hoof +12 (`pf2:1`), **Damage** 2d6+6 bludgeoning"
  - name: "Melee strike"
    desc: "Horn +12 (`pf2:1`) (unarmed), **Damage** 2d8+6 piercing plus [[Knockdown]]"
spellcasting: []
abilities_bot:
  - name: "Pointed Charge"
    desc: "`pf2:2` The bison surges forward at its foe, horns lowered. It Strides twice. If the bison ends its movement within melee range of an enemy, it makes a horn Strike against that enemy. This Strike gains the fatal d12 trait."
  - name: "Rolling Thunder"
    desc: "`pf2:3` The bison kicks up dust and shakes the ground as it charges. <br>  <br> The stampeding bison Strides up to twice its Speed in a straight line, dealing @Damage[(4d6+6)[bludgeoning]|options:area-damage] damage (DC 21 [[Reflex]] save) to any Medium or smaller creature in its path. <br>  <br> Multiple bison can participate in Rolling Thunder by spending this ability's actions and waiting to charge until the herd is ready. Before the beginning of their next turn, they can then charge as a reaction triggered by an adjacent bison beginning its Rolling Thunder charge. All bison in the combined charge must charge in parallel lines, so the areas can't overlap. The combined charge deals an additional 3d6 bludgeoning damage to creatures in the area, and a creature that fails the Reflex saving throw is also knocked [[Prone]]."
  - name: "Knockdown"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Knockdown in its damage entry <br>  <br> **Effect** The monster attempts to `act trip` the creature. This attempt neither applies nor counts toward the monster's multiple attack penalty."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Bison are large bovines with short faces and two horns; they weigh an upwards1 of 2,000 pounds and stand up to 6 feet at the withers. Bison herds thunder across the grassy plains of Golarion, shaking the earth. They're a common sight along the Whistling Plains east of Taldor and the wide grasslands of the nation of Karazh in Casmaron; they also frequently appear in the cooler northeastern reaches of Avistan, the River Kingdoms through Numeria, and the Realm of the Mammoth Lords and western Sarkoris.

Communal by nature, bison gather in large numbers for the summer mating season before the bulls split off to wander the prairie grasses. Bison have adapted well to harsh prairie winters, as their shaggy fur, which grows thicker in winter, insulates them; in the face of blizzards, they survive by facing steadfastly into the howling winds and hunkering down to reduce their exposure.

The way that bison wallow in dirt or rub against large stones might make it easy to mistake their docile nature for passivity. However, this presumption has been the ruin of many hunting parties. Their plentiful meat and thick furs make bison an appealing bounty, but with the ground thundering beneath them, bison can quickly overpower inexperienced hunters unprepared for a stampeding herd. These hunting parties sometimes hire particularly daring adventures, who can add their spells, steel, and expertise to ensure a successful hunt.

While the bison of the plains are the best known and most numerous, they have cousins both in thick boreal forests and along wide, open steppes. These bison variants stand taller but can't match the speed and aggression of their smaller plains relatives.

```statblock
creature: "Bison"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
