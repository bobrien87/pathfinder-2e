---
type: creature
group: ["Aberration", "Air"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Will-o'-Wisp"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Aberration"
trait_02: "Air"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+16; [[Darkvision]]"
languages: "Aklo, Common"
skills:
  - name: Skills
    desc: "Acrobatics +18, Deception +12, Intimidation +12, Stealth +16"
abilityMods: ["-5", "+6", "+0", "+2", "+4", "+2"]
abilities_top: []
armorclass:
  - name: AC
    desc: "27; **Fort** +10, **Ref** +16, **Will** +14"
health:
  - name: HP
    desc: "50"
abilities_mid:
  - name: "Glow"
    desc: "20 feet. <br>  <br> A will-o'-wisp is itself naturally invisible, but glows with a colored light, casting bright light in the aura and making it visible."
  - name: "Magic Immunity"
    desc: "A will-o'-wisp is immune to all spells except [[Force Barrage]], [[Quandary]], and [[Revealing Light]]."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Shock +17 (`pf2:1`) (electricity, magical), **Damage** 2d8+4 electricity"
spellcasting: []
abilities_bot:
  - name: "Feed on Fear"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Requirements** An enemy within 15 feet is under a fear effect or [[Dying]] <br>  <br> **Effect** The will-o'-wisp feeds on the creature's terror. It regains 2d4 healing Hit Points, and if it has Gone Dark, its glow reignites."
  - name: "Go Dark"
    desc: "`pf2:1` The will-o'-wisp extinguishes its glow, becoming [[Invisible]]. It can end this effect with another use of this action. If it uses its shock attack while invisible, the arc of electricity lets any observer determine its location, making the will-o'-wisp only [[Hidden]] to all observers until it moves."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Malevolent balls of colored light, will-o'-wisps haunt lonely marshes and forests, where they lure unsuspecting travelers into danger. Will-o'-wisps can vary the color and illumination they shed, and delight in mimicking bobbing lanterns or distant fires to draw lost or disoriented travelers off of safe trails. They can extinguish their illumination entirely to become [[Invisible]], and they enjoy doing so once their victims are wholly lost and have realized that the bobbing light in the distance isn't, in fact, leading them to safety. Even invisible, however, a will-o'-wisp rarely ventures far from its target, as it feasts upon the panic and dread felt by its victims.

Beneath its glow, a will-o'-wisp's body is a spongy ball approximately 1 foot in diameter and weighing less than 5 pounds. Although most will-o'-wisps are merely translucent, featureless orbs, gaining definition only in the shifting illumination they create, a few have dark mottling that makes them resemble a skull when viewed closely. Will-o'-wisps have no need for mundane nourishment, and in fact, lack the ability to consume matter of any kind; they find all the sustenance they need in the terror of nearby creatures. For this reason, they like to work alongside undead that produce terror in their victims. Will-o'-wisps are long-lived, if not effectively immortal, and they have good memories. A cowed or defeated will-o'-wisp can be a good source of lore and information, though acquiring such cooperation from such a sinister monster is no easy feat.

Will-o'-wisps inhabit desolate swamps and forests and are generally active at twilight and after dark. They are therefore reluctant to lead victims into immediately fatal areas such as deadfalls, but instead prefer hazards where their victims suffer over a long time, such as pockets of stale or poisonous air, patches of quicksand, and dens of bigger monsters. According to will-o'-wisps, different types of fear have subtle differences in flavor. The lurking dread in the pit of the stomach that gnaws at those who slowly become aware of the fact that they're lost produces a much different taste than the sudden, stark terror of imminent death in the face of a towering monster. Because of this, will-o'-wisps try to vary the ways in which they induce terror in their prey, to ensure they don't tire of certain flavors of fear.

```statblock
creature: "Will-o'-Wisp"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
