---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Smilodon"
level: "6"
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
    desc: "+14; [[Low-Light Vision]], [[Scent]] (imprecise) 60 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +12, Athletics +16, Stealth +12"
abilityMods: ["+6", "+2", "+3", "-4", "+2", "+0"]
abilities_top:
  - name: "Sneak Attack"
    desc: "The smilodon deals 1d6 extra precision damage to creatures that are [[Off Guard]]."
armorclass:
  - name: AC
    desc: "23; **Fort** +15, **Ref** +12, **Will** +10"
health:
  - name: HP
    desc: "110"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fangs +16 (`pf2:1`), **Damage** 2d10+6 piercing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Claw +16 (`pf2:1`) (agile, unarmed), **Damage** 2d8+6 slashing plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Pierce Armor"
    desc: "`pf2:1` The smilodon makes a fangs Strike against a creature that's [[Grabbed]] or [[Restrained]]. <br>  <br> If the attack hits, the creature is knocked [[Prone]]; if the creature is wearing armor with hardness 10 or lower, the armor is [[Broken]]. <br>  <br> If this Strike breaks a creature's armor or damages a creature who is unarmored or wearing broken armor, the creature also takes 2d6 bleed. This Strike doesn't further damage armor that's already broken."
  - name: "Pounce"
    desc: "`pf2:1` The smilodon Strides and makes a Strike at the end of that movement. If the smilodon began this action [[Hidden]], it remains hidden until after this ability's Strike."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Smilodons are large saber-toothed cats, apex predators that are significantly more muscular and broader than the other species of big cats. They often kill prey with a quick stab to the throat or other vulnerable spot. The smilodon's oversized fangs are particularly sought after as trophies.

Few predators of the natural world can match the cat's talent for stalking and stealth. Large cats can be found in almost any environment, usually keeping their distance from settlements. When civilization encroaches onto a big cat's hunting grounds, the animals are often driven to making desperate attacks against unwary travelers.

```statblock
creature: "Smilodon"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
