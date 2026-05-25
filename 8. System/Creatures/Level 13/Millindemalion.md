---
type: creature
group: ["Fey"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Millindemalion"
level: "13"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Fey"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+23; [[Low-Light Vision]]"
languages: "Aklo, Common, Fey"
skills:
  - name: Skills
    desc: "Crafting +28, Occultism +24, Society +24, Stealth +27, Millinery Lore +30"
abilityMods: ["+4", "+8", "+1", "+7", "+4", "+2"]
abilities_top:
  - name: "Sneak Attack"
    desc: "A millindemalion deals an extra 4d6 precision damage to [[Off Guard]] creatures."
armorclass:
  - name: AC
    desc: "33; **Fort** +20, **Ref** +27, **Will** +23"
health:
  - name: HP
    desc: "275; **Weaknesses** cold iron 10"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` The millindemalion can use Hat Toss against the triggering creature instead of making a Strike, making a melee attack roll with a Millindemalion hat toss check{+27} modifier to do so. <br>  <br> **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
  - name: "Unsettling Mind"
    desc: "Attempting to touch the frenetic mind of a millindemalion is a dangerous task. When the millindemalion succeeds at a saving throw against a mental effect, the creature originating that effect takes 4d6 mental damage."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Felt Shears +27 (`pf2:1`) (deadly d8, finesse, magical, versatile p), **Damage** 2d4+14 piercing plus 1d6 mental"
spellcasting: []
abilities_bot:
  - name: "Hat Toss"
    desc: "`pf2:1` The millindemalion quickly crafts a mind-altering hat in combat and tosses it onto a target with a flick of their wrist. The millindemalion chooses one of the effects below and makes a ranged attack roll with a Millindemalion hat toss check{+27} modifier and a range increment of 20 feet. <br>  <br> On a hit, the target must succeed at a DC 33 [[Will]] save saving throw or experience the listed effect for 1d4+1 rounds. If the millindemalion critically succeeds at the ranged Strike, the target takes a -4 circumstance penalty on the save. <br>  <br> A target can only wear one millindemalion hat at a time; a new hat replaces any previous hat. The hat can't be removed before the condition ends, but when the condition ends (or on a successful save), the hat falls to pieces. <br>  <br> - **Befuddling Bowler** The hat clouds the target's mind; the target becomes [[Stupefied 2]]. <br> - **Bewitching Beret** The target is infatuated with their new hat and its creator, becoming [[Fascinated]] by the millindemalion and the beret. <br> - **Dazzling Deerstalker** The target can barely see with the hat falling down over its eyes and gains the [[Dazzled]] condition. <br> - **Fettering Fedora** The target feels a heavy weight pressing down on them from the hat and takes a -10-foot circumstance penalty to their Speeds. <br> - **Tiring Tricorne** The target grows sleepy and becomes [[Slowed]] 1. <br>  <br> > [!danger] Effect: Fettering Fedora"
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Millindemalion are cruel fey tricksters capable of causing mayhem with their magical, mind-altering hats. Many folk tales from around the world speak of industrious fey who help struggling crafters-cobblers, milliners, tailors, and so on-during the night, creating quality wares in secret for no payment greater than a crumb of bread or a saucer of cream. These stories hold a grain of truth, as gracious fey do occasionally journey from the First World to aid a humble artisan on a whim, for bribes of food, or sometimes even as part of a concerted effort to spread beauty throughout the world. However, when an artisan becomes too reliant on this help, their friendly fey helper might become warped and twisted with resentment and neglect. Eventually, they could transform into a cruel prankster who delights in punishing mortals who dare task a fey with such mundane work. The millindemalion is the result of a kindly, hat-making fey undergoing such a transformation. Some scholars believe this erratic behavior is caused by the preponderance of quicksilver used in most millinery.

```statblock
creature: "Millindemalion"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
