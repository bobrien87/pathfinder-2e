---
type: creature
group: ["Aberration"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Divoynik"
level: "3"
rare_01: "Uncommon"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Aberration"
trait_02: ""
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+7; [[Darkvision]]"
languages: "Common (Two other languages, Telepathy 100 feet)"
skills:
  - name: Skills
    desc: "Acrobatics +8, Athletics +8, Deception +11, Diplomacy +9, Intimidation +9, Society +8, Stealth +10"
abilityMods: ["+3", "+3", "+0", "+1", "+2", "+4"]
abilities_top:
  - name: "Telepathy 100 feet"
    desc: "A monster with telepathy can communicate mentally with any creatures within the listed radius, as long as they share a language. This doesn't give any special access to their thoughts, and communicates no more information than normal speech would."
armorclass:
  - name: AC
    desc: "18; **Fort** +6, **Ref** +10, **Will** +11"
health:
  - name: HP
    desc: "45; **Immunities** bleed, polymorph"
abilities_mid:
  - name: "Cracked Mirror"
    desc: "A divoynik has weakness 3 to physical attacks made by a creature whose form they're mimicking, and the mimicked creature gains weakness 3 to physical attacks made by the divoynik."
  - name: "Savor Anguish"
    desc: "`pf2:r` **Trigger** A creature within 30 feet of the divoynik fails a saving throw against an emotion effect <br>  <br> **Effect** The divoynik feeds on their victim's mental distress, gaining 5 temporary Hit Points for up to 1 minute. They can feed on a given creature's emotions only once every 24 hours."
  - name: "Sudden Betrayal"
    desc: "A divoynik can always use Deception when rolling initiative, as long as at least one enemy doesn't know their true nature. On the first round of combat, if the divoynik rolled Deception for initiative, creatures that haven't acted are [[Off Guard]] to the divoynik."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Fist +11 (`pf2:1`) (agile), **Damage** 1d10+5 bludgeoning"
spellcasting:
  - name: "Occult Innate Spells"
    desc: "DC 20, attack +0<br>**3rd** [[Mind Reading]] (At Will)"
abilities_bot:
  - name: "Change Shape"
    desc: "`pf2:1` The divoynik can take on the specific appearance of any Small or Medium animal or humanoid they've seen. This doesn't change their Speed or their attack and damage bonuses with their Strikes, but it might change the damage type their Strikes deal (such as to slashing with a claw). <br>  <br> The monster changes its shape indefinitely. It can use this action again to return to its natural shape or adopt a new shape. Unless otherwise noted, a monster cannot use Change Shape to appear as a specific individual. Using Change Shape counts as creating a disguise for the [[Impersonate]] use of Deception. The monster's transformation automatically defeats Perception DCs to determine whether the creature is a member of the ancestry or creature type into which it transformed, and it gains a +4 status bonus to its Deception DC to prevent others from seeing through its disguise. Change Shape abilities specify what shapes the monster can adopt. The monster doesn't gain any special abilities of the new shape, only its physical form. For example, in each shape, it replaces its normal Speeds and Strikes, and might potentially change its senses or size. Any changes are listed in its stat block."
  - name: "Window to the Soul"
    desc: "`pf2:1` The divoynik meets the gaze of a creature within 60 feet whose form they've taken with their Change Shape ability. The target must attempt a DC 20 [[Will]] save saving throw. <br> - **Critical Success** The target is unaffected and immune for 24 hours. <br> - **Success** The target is unaffected. <br> - **Failure** The target is [[Fascinated]] for 1 minute. Hostile actions do not end this fascination, but if the divoynik Changes Shape, moves out of range, or is no longer visible to the target, the fascination immediately ends. While fascinated, the target takes a –1 circumstance penalty to Will saves against the divoynik's spells and abilities. <br> - **Critical Failure** As failure, and the divoynik can spend a free action to telepathically extract the answer to one question from the target. The target can attempt a DC 20 [[Deception]] check to attempt to evade the query and give misleading information."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

A close-knit settlement is rocked to its core when a beloved pillar of the community is accused of a heinous crime. The accused protest their innocence, but overwhelming evidence leaves no room for doubt. As justice is served, the community is irreversibly changed, its neighborly atmosphere giving way to lingering paranoia—the favored fare of the divoynik.

Divoyniks are malevolent shapeshifters, capable not only of mimicking the physical appearance of other creatures but also of plucking thoughts and memories from their victims' minds. A divoynik retains their most recently assumed guise even after death. Spells like ring of truth help see through a divoynik, and truesight reveals its shapeshifted nature, making clear otherwise imperceptible markings similar to an animal's stripes on a divoynik's body. Beyond magic, people who encounter a divoynik can always rely on one other method of identification. Although identical to their mimicked form in all other respects, a divoynik's body contains neither blood nor a heart.

```statblock
creature: "Divoynik"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
