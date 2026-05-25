---
type: creature
group: ["Humanoid", "Tanuki"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Tanuki Village Hero"
level: "1"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Small"
trait_01: "Humanoid"
trait_02: "Tanuki"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+4"
languages: "Common, Tanuki"
skills:
  - name: Skills
    desc: "Athletics +5, Diplomacy +6, Stealth +6, Legal Lore +3"
abilityMods: ["+2", "+3", "+2", "+0", "-1", "+3"]
abilities_top: []
armorclass:
  - name: AC
    desc: "16; **Fort** +7, **Ref** +8, **Will** +2"
health:
  - name: HP
    desc: "21"
abilities_mid:
  - name: "Tactical Retreat"
    desc: "`pf2:r` **Trigger** The tanuki takes damage <br>  <br> **Effect** The tanuki runs to a better tactical position. The tanuki gains the [[Fleeing]] condition until the beginning of their next turn and Strides."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Kama +7 (`pf2:1`) (agile, trip), **Damage** 1d6+2 slashing"
  - name: "Melee strike"
    desc: "Dart +8 (`pf2:1`) (agile, thrown 20), **Damage** 1d4+2 piercing"
spellcasting: []
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The tanuki takes on the form of a mundane raccoon dog. This makes them Tiny and gives them a +2 status bonus to their Stealth modifier, but they can't make Strikes. <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Tricky Throw"
    desc: "`pf2:2` The tanuki winds up and puts their everything into a throw. They make a dart Strike at one enemy within 40 feet. If the Strike is unsuccessful, the tanuki falls [[Prone]]. If the Strike is successful, they really did put everything into the throw, having transformed into the dart the moment they threw it. The tanuki disappears from the space they threw from, appears in a space adjacent to the enemy and makes a kama Strike against said enemy, who's [[Off Guard]] to the attack."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

A tanuki village hero is a firefighter, monster slayer, peacekeeper, and altruist. Village heroes are elected by community vote; while the village hero sometimes grumbles that it's a lot of responsibility for a single tanuki to bear, the community insists there's no higher honor than to be trusted with their well-being.

Tanuki are an ancestry of humanoids resembling raccoons or canids who live primarily in Minkai, in Tian Xia, though they are also found in Hwanggot and the successor states of Lung Wa. Tanuki outside of Minkai tend to be shier, keeping to their raccoon-dog forms and staying out of trouble, and so most people associate tanuki solely with the boisterous and mischievous communities found in Minkai.

Perennial underdogs, most tanuki live for feasting, festivals, and fun, which they accomplish mainly through their wide range of shapeshifting powers. They are especially known for pranks that tend to backfire in their faces, from posing as teapots for a quick profit (and then immediately being set on fire by new owners seeking to make tea) to posing as priests (and being promptly exorcised by the real priests with whom they attempt to blend in.) Despite this, tanuki are masters at rolling with any punches that life flings at them.

Many tanuki see other shapechangers as rivals, especially kitsune, which are also common in Minkai. Such tanuki are [[Prone]] to creating impromptu competitions to prove their ancestry's superiority at shapechanging. These competitions are always meant to be good natured, at least for the competitors; bamboozled villagers caught up in the wake of these games often have different opinions.

Somewhat confusingly, the animals that tanuki resemble are also known as tanuki, and it is difficult to ascertain whether any individual raccoon dog is a simple beast or a sapient tanuki in disguise.

Transformation DuelsTanuki often settle disputes with transformation contests. The competitors' objective is to fool their opponent with a combination of assumed form and clever ruse. Legends tell of rivals transforming into flotillas of ships or imperial processions, or cunningly tricking their opponent into thinking they did.

```statblock
creature: "Tanuki Village Hero"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
