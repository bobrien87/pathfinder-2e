---
type: creature
group: ["Aberration", "Time"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Hound of Tindalos"
level: "7"
rare_01: "Rare"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Aberration"
trait_02: "Time"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+17; [[Greater Darkvision]]"
languages: "Aklo"
skills:
  - name: Skills
    desc: "Acrobatics +17, Athletics +15, Occultism +17, Stealth +17, Survival +13"
abilityMods: ["+4", "+6", "+2", "+6", "+4", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "25; **Fort** +13, **Ref** +17, **Will** +15"
health:
  - name: HP
    desc: "90; **Immunities** controlled, emotion; **Resistances** mental 10, physical 10, poison 10"
abilities_mid:
  - name: "Otherworldly Mind"
    desc: "Whenever a creature targets the hound with a mental effect, that creature takes 4d6 mental damage (DC 25 [[Will]] save). On a critical failure, it also becomes [[Confused]] for 1d4 rounds."
  - name: "Ripping Gaze"
    desc: "30 feet. The hound of Tindalos's eyes glow balefully, causing painful but bloodless wounds to rip open in the body of a creature that meets its awful gaze. When a creature ends its turn in the aura's emanation, it takes 4d6 slashing damage (DC 25 [[Fortitude]] save). <br>  <br> A creature that critically succeeds at its save is temporarily immune for 24 hours."
  - name: "Vulnerable to Curved Space"
    desc: "When a hound of Tindalos is not adjacent to a structural angle of 90º (or more acute), its resistance to physical damage is suppressed and it becomes [[Sickened]] 1. It can't recover from this sickened condition, but the condition ends automatically once the hound is again adjacent to a suitable angle. <br>  <br> > [!danger] Effect: Vulnerable to Curved Space"
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +17 (`pf2:1`), **Damage** 2d10+7 piercing"
  - name: "Melee strike"
    desc: "Claw +17 (`pf2:1`) (agile), **Damage** 2d8+7 slashing"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 21, attack +13<br>**8th** [[Pinpoint]]<br>**4th** [[Planar Tether]]<br>**3rd** [[Haste]], [[Slow]]<br>**2nd** [[Invisibility (Self Only)]]"
abilities_bot:
  - name: "Angled Entry"
    desc: "`pf2:1` The hound of Tindalos casts a 4th-rank [[Translocate]] spell, but it must transport itself into a space adjacent to an angle of 90° (or more acute) in the structure or environment around it. For example, it could teleport to a space adjacent to a wall (using the angle between the wall and floor) or a corner in a room, or adjacent to a sizable tree growing straight up out of the ground, but not to a flat plain or a room with only curved corners and edges. <br>  <br> Once per day, the hound can use this ability to interplanar teleport to or from the Dimension of Time, with the same restrictions on what angles it can appear next to."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Lean and athirst, the hounds of Tindalos are drawn to those who tamper with the flow of time, travel through time, or use magic or rare alchemical drugs to send their thoughts or perception backward or forward in time. Powerful spellcasters can draw them from the Dimension of Time via rare rituals, but doing so attracts the hounds' ire, so few who traffic in such rituals live long enough to spread their knowledge. While the hounds possess great cunning and cruel intellect, they rarely interact with other creatures—other than to hunt and destroy those who've attracted their unblinking attention.

Once a hound catches the scent of a mortal to hunt, it calls others of its ilk. The pack then pursues its victim through all space and time until it catches, slays, and devours them. Those pursued can escape only by avoiding all angles, as hounds of Tindalos could step through them from nothingness at any time.

```statblock
creature: "Hound of Tindalos"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
