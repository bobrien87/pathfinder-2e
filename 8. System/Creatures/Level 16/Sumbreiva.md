---
type: creature
group: ["Humanoid", "Unholy"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Sumbreiva"
level: "16"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Large"
trait_01: "Humanoid"
trait_02: "Unholy"
trait_03: "Void"
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+29; [[Greater Darkvision]], [[Scent]] (imprecise) 30 feet"
languages: "Aklo, Necril"
skills:
  - name: Skills
    desc: "Athletics +28, Intimidation +30, Stealth +35, Survival +29"
abilityMods: ["+8", "+9", "+3", "+6", "+5", "+4"]
abilities_top:
  - name: "Huntblade Brutality"
    desc: "The sumbreiva's huntblade deals an additional 2d8 precision damage to [[Drained]], [[Frightened]], or [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "39; **Fort** +25, **Ref** +33, **Will** +27"
health:
  - name: HP
    desc: "290; void healing; **Immunities** death effects, drained"
abilities_mid:
  - name: "Hunter's Triumph"
    desc: "`pf2:r` **Trigger** The sumbreiva kills a creature <br>  <br> **Effect** The sumbreiva lets out a triumphant, bone-chilling howl. Every enemy in a @Template[type:emanation|distance:30] must succeed at a DC 36 [[Will]] save or become [[Frightened]] 3 (and [[Fleeing]] as long as it's frightened on a critical failure)."
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Improved Grab"
    desc: "`pf2:0` **Trigger** The monster's last action was a successful Strike that lists Improved Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with as a free action. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Improved Grab as an action and choose one creature it's grabbing or restraining with an appendage that has Improved Grab to automatically extend that condition to the end of the monster's next turn."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Sumbreiva Huntblade +33 (`pf2:1`) (agile, death, finesse, magical, versatile s), **Damage** 3d8+16 piercing plus [[Huntblade Brutality]]"
  - name: "Melee strike"
    desc: "Sumbreiva Huntblade +33 (`pf2:1`) (agile, death, magical, thrown 30, versatile s), **Damage** 3d8+16 piercing plus [[Huntblade Brutality]]"
  - name: "Melee strike"
    desc: "Shadow Whip +33 (`pf2:1`) (agile, death, disarm, finesse, magical, reach 10 ft., trip), **Damage** 3d4+16 bludgeoning plus [[Improved Grab]]"
spellcasting:
  - name: "Arcane Innate Spells"
    desc: "DC 36, attack +28<br>**3rd** [[Earthbind]]<br>**2nd** [[Darkness]]"
abilities_bot:
  - name: "Claim Trophy"
    desc: "`pf2:1` The sumbreiva claims the soul of a creature they killed within the last minute. This works like [[Seize Soul]], except that no black sapphire is required, and the soul is turned into a glowing blue light called a soul trophy. Anyone who kills the sumbreiva can then free the soul from any soul trophy by touching it and speaking the word for \"freedom\" in any language."
  - name: "Whip Drain"
    desc: "`pf2:1` **Requirements** The sumbreiva has a creature [[Grabbed]] with their shadow whip <br>  <br> **Effect** The grabbed creature must succeed at a DC 38 [[Fortitude]] save or become [[Drained]] 2 ([[Drained]] 3 on a critical failure). If the creature is already drained, this increases its drained value instead, to a maximum of [[Drained]] 4."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Sumbreivas are the Void's unstoppable hunters, tracking down and destroying other creatures on their plane for sport and practice. Occasionally, they pass through a rift or are brought to the Universe via a binding circle, where they collect living souls to display as trophies.

Sumbreivas gather at Night Lodges, where they train and display their soul trophies, which appear as floating wisps of blue energy. The more formidable the soul, the more intense the blue glow that emanates from it. Sumbreivas in lodges periodically raid the Universe on a Night Hunt and compete to see who can bring back the most brilliant soul trophies. The winner of the Night Hunt leads the lodge until the next hunt. Night Lodges are ranked against each other by the accomplishments of the hunters within. All sumbreivas desire to capture a soul powerful enough to earn them placement in the Twilight Lodge, reserved for the truly elite souls and hunters.

```statblock
creature: "Sumbreiva"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
