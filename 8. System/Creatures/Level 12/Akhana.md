---
type: creature
group: ["Aeon", "Monitor"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Akhana"
level: "12"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Aeon"
trait_02: "Monitor"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+27; [[Darkvision]], [[Lifesense]] (precise) 120 feet"
languages: "Envisioning"
skills:
  - name: Skills
    desc: "Acrobatics +25, Athletics +24, Medicine +23, Occultism +21, Religion +23, Axis Lore +23"
abilityMods: ["+6", "+6", "+7", "+3", "+5", "+4"]
abilities_top:
  - name: "Envisioning"
    desc: "100 feet <br>  <br> An akhana can communicate mentally with any creatures in the aura using wordless psychic projections. They don't need to share a language, though the aeon's meaning to non-aeons can be vague and is often mysterious. An aeon can use this ability to communicate flawlessly with any other aeon on the same plane as itself."
  - name: "At-Will Spells"
    desc: "The monster can cast its at-will spells any number of times without using up spell slots."
armorclass:
  - name: AC
    desc: "32; **Fort** +23, **Ref** +22, **Will** +23"
health:
  - name: HP
    desc: "225; **Immunities** vitality, void; **Weaknesses** spirit 10"
abilities_mid:
  - name: "+1 Status to All Saves vs. Magic"
    desc: ""
  - name: "Balance Life"
    desc: "`pf2:r` **Trigger** A creature within 100 feet is about to attempt a recovery check <br>  <br> **Effect** The akhana chooses to make the result a success or failure (but not a critical success or failure). This effect gains the fortune trait if the akhana chooses success or misfortune for failure."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Tail +24 (`pf2:1`) (magical, void), **Damage** 5d10 void plus [[Grab]]"
  - name: "Melee strike"
    desc: "Fist +24 (`pf2:1`) (agile, magical, unarmed), **Damage** 3d6+12 bludgeoning"
spellcasting:
  - name: "Divine Innate Spells"
    desc: "DC 32, attack +24<br>**2nd** [[Peaceful Rest]]<br>**1st** [[Harm]] (At Will), [[Heal]] (At Will), [[Stabilize]], [[Vitality Lash]], [[Void Warp]]"
abilities_bot:
  - name: "Flying Fists"
    desc: "`pf2:2` The akhana Flies and makes up to four fist Strikes against different targets at any points during this movement. The attacks count toward its multiple attack penalty normally, but the penalty does not increase until after Flying Fists is complete."
  - name: "Reclaim Life"
    desc: "`pf2:1` **Requirements** The akhana has a living creature [[Grabbed]] or [[Restrained]] with its tail <br>  <br> **Effect** The creature takes 4d10 void damage with a DC 32 [[Fortitude]] save. On a failed save, it's also [[Doomed]] 1. If the creature dies while doomed and held in the akhana's tail, its soul is trapped in the akhana (as [[Seize Soul]]), and its remains are preserved as peaceful rest. The soul returns to the body with 1 Hit Point if the akhana [[Dismisses]] the effect, if the akhana is slain, or if a [[Wish]] ritual or similarly powerful magic frees it."
  - name: "Sprout Life"
    desc: "`pf2:2` A @Template[burst|distance:5] within 100 feet fills with simple life appropriate to the environment. The newly forged animals bite those in the area for @Damage[7d6[piercing]|options:area-damage] damage with a DC 32 [[Reflex]] save. The akhana can also have fungus or plants choke the area, even floating ones in the sky, creating difficult terrain. The created life lives or dies normally after its creation."
  - name: "Grab"
    desc: "`pf2:1` **Requirements** The monster's last action was a successful Strike that lists Grab in its damage entry, or the monster has a creature [[Grabbed]] or [[Restrained]] <br>  <br> **Effect** If used after a Strike, the monster attempts to `act grapple` the creature using the body part it attacked with. This attempt neither applies nor counts toward the creature's multiple attack penalty. <br>  <br> The monster can instead use Grab and choose one creature it's grabbing or restraining with an appendage that has Grab to automatically extend that condition to the end of the monster's next turn."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

Akhanas are massive eyes formed of cosmic matter that monitor the balance of birth and death. They understand the profound influence living things have on the cosmos and silently perform their duties of supporting and pruning life. Akhanas seem utterly unconcerned by the fate of souls after death, often leaving undead in their wake or attracting daemon scavengers. Psychopomps often despair over akhanas' cryptic actions, forced to clear out sudden backlogs of souls or even battle the aeons directly. Their "tail" is a twisting column of cosmic energy that can drain vitality from creatures and seal their fate.

Aeons have always been the caretakers of reality and defenders of the natural order of balance. Each type of aeon takes on some form of duality in its manifestation and works either to shape the multiverse within the aspects of this duality in some way, or to correct imbalances to the perfect order of existence. Aeons' machinations can raise a nation, raze it, or restore it from ruin. Their reasons are their own, and they rarely share their motivations with others—through their strange envisioning mode of communication, they simply create the results they insist are necessary to maintain the balance of the multiverse.

As a result of recent shifts in reality, aeons have begun to reassert a presence in the perfect planar city of Axis. To aeons, this is merely the latest in a recurring cycle, albeit one that mortals have not yet borne witness to. Aeons have a name for this cyclic return, in which they welcome their industrious axiomite brethren back to their fold: the Convergence. At the onset of the Convergence, a council of pleroma aeons appeared in the Eternal City of Axis, where they revealed that axiomites were wayward aeons, split off long ago to pursue the act of creation. With the latest cycle of change, it was time for axiomites—and their mortal creations and kin—to rejoin the aeon cause. While most axiomites fell in line, realizing perhaps on a fundamental level of reality that what the aeons said was the truth, some refused to heed the call and waited for the wrath of the aeons. That wrath has yet to come. The dual-natured aeons have responded to those who have declined in confusing ways. With some they treat and even bargain, while a handful of others they have destroyed, and a few have been exterminated by the axiomites. But most of these quiet insurgents they leave alone, allowing these axiomites to continue to create in peace. How—or if—this Convergence will end is as little understood as aeons themselves.

```statblock
creature: "Akhana"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
