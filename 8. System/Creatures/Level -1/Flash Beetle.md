---
type: creature
group: ["Animal"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Flash Beetle"
level: "-1"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Animal"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+6; [[Low-Light Vision]]"
languages: ""
skills:
  - name: Skills
    desc: "Acrobatics +6, Athletics +4"
abilityMods: ["+1", "+3", "+2", "-5", "+1", "-2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "16; **Fort** +5, **Ref** +8, **Will** +4"
health:
  - name: HP
    desc: "6"
abilities_mid:
  - name: "Luminescent Aura"
    desc: "10 feet. <br>  <br> The flash beetle's bioluminescent organs fill the area with bright light."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Mandibles +8 (`pf2:1`) (agile, finesse), **Damage** 1d4+1 piercing"
spellcasting: []
abilities_bot:
  - name: "Light Flash"
    desc: "`pf2:1` The flash beetle creates a brilliant flash of light. All creatures in its luminescent aura must succeed at a DC 17 [[Fortitude]] save or be [[Dazzled]] for 1 minute. <br>  <br> The flash beetle's glow then goes out, disabling its aura for 24 hours, during which time it cannot use Light Flash."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

These 3-foot-long insects boast a pair of glowing organs on the back of the abdomen that give off bright light and that continue to glow for days, even after the creature's death. Flash beetles are commonly herded and harvested by miners and spelunkers, as their glow is considered safer than torches and less expensive than lamps. Denizens of the Darklands often domesticate and train these insects, using them as pets, livestock, or caging them to use as organic sources of light in areas frequented by visitors unaccustomed to the darkness.

Not all beetles are harmless creatures that can be easily crushed underfoot. Oversized and ravenous giant beetles can be found throughout the temperate and tropical regions of the world. They are often benign creatures, though when threatened or roused, giant beetles are quite dangerous. Their powerful mandibles and tough exoskeletons make for a challenging combatant.

```statblock
creature: "Flash Beetle"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
