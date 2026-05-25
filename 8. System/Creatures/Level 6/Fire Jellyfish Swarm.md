---
type: creature
group: ["Animal", "Aquatic"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Fire Jellyfish Swarm"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Animal"
trait_02: "Aquatic"
trait_03: "Mindless"
trait_04: "Swarm"
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+11; [[Low-Light Vision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +15"
abilityMods: ["-4", "+5", "+4", "-5", "+0", "-5"]
abilities_top:
  - name: "Agile Swimmer"
    desc: "Fire jellyfish swarms use Acrobatics to [[Swim]]."
  - name: "Fire Jelly Venom"
    desc: "**Saving Throw** DC 24 [[Fortitude]] save <br>  <br> **Maximum Duration** 6 rounds <br>  <br> **Stage 1** [[Clumsy]] 1 (1 round) <br>  <br> **Stage 2** [[Clumsy]] 2 (1 round) <br>  <br> **Stage 3** [[Clumsy]] 3 (1 round)"
armorclass:
  - name: AC
    desc: "13; **Fort** +16, **Ref** +15, **Will** +10"
health:
  - name: HP
    desc: "155; **Immunities** critical hits, precision, swarm mind; **Weaknesses** area damage 7, splash damage 7; **Resistances** bludgeoning 9, piercing 9, poison 10, slashing 5"
abilities_mid:
  - name: "Swarm Mind"
    desc: "This monster doesn't have a single mind (typically because it's a swarm of smaller creatures), and is immune to mental effects that target only a specific number of creatures. It is still subject to mental effects that affect all creatures in an area."
speed: "0 feet"
attacks: []
spellcasting: []
abilities_bot:
  - name: "Burning Swarm"
    desc: "`pf2:1` Each enemy in the swarm's space takes 3d8 poison damage (DC 24 [[Reflex]] save) and is exposed to fire jelly venom."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

While individually one of these fist-sized jellyfish is merely a nuisance, in great numbers, fire jellyfish can form into dangerous swarms. Bobbing in the water, they create a cloud of stinging tentacles. They were named in part for their bright coloration, but those who are stung by fire jellyfish learn the larger reason for their name—the pain of their stings is comparable to being burned alive.

Many varieties of jellyfish drift through the world's oceans, feeding on fish and other tiny marine creatures. However, deadly species of monstrous jellyfish pose a threat to unwary swimmers and sailors alike. Note that while jellyfish are animals, they also have the mindless trait because they lack a centralized nervous system.

```statblock
creature: "Fire Jellyfish Swarm"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
