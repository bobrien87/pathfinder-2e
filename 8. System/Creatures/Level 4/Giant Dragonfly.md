---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Giant Dragonfly"
level: "4"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+11; [[Darkvision]], [[Wavesense]] (imprecise) 30 feet"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +10, Athletics +10, Stealth +12"
abilityMods: ["+4", "+4", "+2", "-5", "+3", "+0"]
abilities_top:
  - name: "Snatch"
    desc: "The giant dragonfly can Fly at half Speed while it has a creature [[Grabbed]] or [[Restrained]] by Clutch, carrying that creature along with it."
armorclass:
  - name: AC
    desc: "21; **Fort** +12, **Ref** +14, **Will** +9"
health:
  - name: HP
    desc: "60"
abilities_mid: []
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Mandibles +14 (`pf2:1`), **Damage** 1d12+7 piercing plus [[Grab]]"
spellcasting: []
abilities_bot:
  - name: "Clutch"
    desc: "`pf2:1` **Requirements** The giant dragonfly has a Medium or smaller creature [[Grabbed]] in its mandibles <br>  <br> **Effect** The dragonfly tries to transfer the grabbed creature to be clutched by its legs. The giant dragonfly attempts an Athletics check against the creature's Reflex DC. On a success, it transfers the creature (which remains grabbed) to its legs, freeing its mandibles to attack. The dragonfly can have only one creature clutched at a time."
  - name: "Swoop"
    desc: "`pf2:2` The giant dragonfly Flies up to its Speed and makes one mandible Strike at any point during that movement."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

These buzzing insects are the size of a small horse. They're ambush predators that hunt beasts and humanoids alike, capable of using impressive aerial acrobatics to swoop down from above and snatch away their prey.

Dragonflies hunt with a combination of agile power and deadly speed. In early life stages, these insects are entirely aquatic predators, but they take to the air once they've molted. Most live around bodies of water suitable for spawning, but giant dragonflies have been known to fly many miles while on the hunt. Though their gossamer wings and colorful bodies are beautiful at first glance, an unwary adventurer lured in by the display runs a very real risk of becoming lunch.

```statblock
creature: "Giant Dragonfly"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
