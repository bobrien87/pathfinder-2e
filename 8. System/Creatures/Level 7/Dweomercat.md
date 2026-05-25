---
type: creature
group: ["Beast"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Dweomercat"
level: "7"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Beast"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+15; [[Darkvision]], [[Scent]] (imprecise) 30 feet"
languages: "Common, Fey"
skills:
  - name: Skills
    desc: "Acrobatics +17, Arcana +16, Nature +15, Stealth +17, Survival +15"
abilityMods: ["+4", "+4", "+3", "+3", "+4", "+5"]
abilities_top: []
armorclass:
  - name: AC
    desc: "25; **Fort** +12, **Ref** +17, **Will** +17"
health:
  - name: HP
    desc: "100"
abilities_mid:
  - name: "Alter Dweomer"
    desc: "`pf2:r` **Trigger** The dweomercat is targeted by a spell or is within the area of a spell as it's cast <br>  <br> **Effect** The dweomercat's runelike patterns start to glow as it gains an effect related to the tradition of the triggering spell. This effect occurs before the dweomercat is affected by the triggering spell. The effect lasts for 1 minute, until the dweomercat uses this ability again, or until the dweomercat Dismisses the effect, whichever comes first. <br>  <br> - **Arcane** Magical feedback deals 4d6 force damage to the triggering spellcaster (DC 22 [[Reflex]] save). <br> - **Divine** The dweomercat gains a +1 status bonus to all skill checks. <br> - **Occult** The dweomercat becomes [[Invisible]]. This effect ends if the dweomercat uses a hostile action, in addition to the normal end conditions. <br> - **Primal** The dweomercat gains 10 temporary Hit Points."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +17 (`pf2:1`) (magical), **Damage** 2d10+7 piercing plus [[Grab]]"
  - name: "Melee strike"
    desc: "Claw +17 (`pf2:1`) (agile, magical), **Damage** 2d8+7 slashing"
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 25, attack +17<br>**4th** [[Dispelling Globe]], [[Translocate]]<br>**2nd** [[Dispel Magic]] (At Will)<br>**1st** [[Detect Magic]]"
abilities_bot:
  - name: "Dweomer Leap"
    desc: "`pf2:2` Prerequisites The dweomercat has at least one [[Translocate]] spell remaining <br>  <br> **Effect** The dweomercat casts *translocate*, then can make a melee Strike against one creature adjacent to it at the end of its teleport. If the dweomercat ends its teleport adjacent to a creature under an ongoing spell effect or who cast a spell since the dweomercat's last turn, this does not expend a casting of *translocate*."
  - name: "Pounce"
    desc: "`pf2:1` The dweomercat Strides and makes a Strike at the end of that movement. If the dweomercat began this action [[Hidden]], it remains hidden until after this ability's Strike."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Dweomercats are magically gifted, four-eyed felines from the First World, where they prey upon other creatures and feed on their primal energy. Within the First World, they form packs that hunt together, though they prefer to care for their cubs on their own, raising them on a diet of magic and magical creatures. Curious creatures, they're sometimes encountered in areas of the Universe where the veil to the First World is thin or in regions where magic has been irreparably warped. Drawn there by the unique magical resonance, the dweomercats hope to acquire incomparable sources of food.

Where dweomercats sighting have been reported, specialized trappers will appear soon after, hoping for the catch of a lifetime. A dweomercat's dark purple fur is prized by magical collectors, as the patterns that flow through the fur appear as though they were hand-painted, with spirals and curls resembling magical runes. These coats are then either displayed or included as components in rare rituals. Dweomercats are famous for their ability to twist the metaphorical strings of spells cast on or near them, which they can transform into their own defensive magic or use to instantly teleport across the battlefield.

```statblock
creature: "Dweomercat"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
