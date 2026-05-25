---
type: creature
group: ["Humanoid", "Nagaji"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Nagaji Soldier"
level: "2"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Humanoid"
trait_02: "Nagaji"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+8; [[Low-Light Vision]]"
languages: "Common, Draconic"
skills:
  - name: Skills
    desc: "Athletics +8, Intimidation +5, Nature +6, Religion +5"
abilityMods: ["+4", "+1", "+3", "-1", "+2", "+1"]
abilities_top: []
armorclass:
  - name: AC
    desc: "18; **Fort** +9, **Ref** +7, **Will** +6"
health:
  - name: HP
    desc: "28; **Resistances** poison 2"
abilities_mid:
  - name: "Reactive Strike"
    desc: "`pf2:r` **Trigger** A creature within the monster's reach uses a manipulate action or a move action, makes a ranged attack, or leaves a square during a move action it's using. <br>  <br> **Effect** The monster attempts a melee Strike against the triggering creature. If the attack is a critical hit and the trigger was a manipulate action, the monster disrupts that action. This Strike doesn't count toward the monster's multiple attack penalty, and its multiple attack penalty doesn't apply to this Strike."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Khopesh +10 (`pf2:1`) (trip), **Damage** 1d8+4 slashing"
  - name: "Ranged strike"
    desc: "Longbow +7 (`pf2:1`) (deadly d10, volley 30, range 100 ft.), **Damage** 1d8 piercing"
spellcasting: []
abilities_bot:
  - name: "Slough Toxins"
    desc: "`pf2:1` **Frequency** once per round <br>  <br> **Requirements** The nagaji is afflicted with a poison <br>  <br> **Effect** The nagaji accelerates their metabolism. They roll a saving throw against the affliction with a +2 circumstance bonus. If they must attempt an ongoing save against the same poison at the end of their turn, they also get a +2 circumstance bonus to that save."
sourcebook: "Monster Core 2"
source-type: "Remaster"
---
### `= this.file.name`

Nagaji are lithe but muscular bipeds with humanoid figures and serpentine heads. Their bodies are covered in tightly layered scales that range wildly in color, from camouflaged greens and browns to flashy blues or reds. Ophidian eyes lend nagaji an imperious visage, with irises that span every color of the rainbow. Nagaji don't blink, which has been known to unsettle other ancestries whether a nagaji intends it or not.

Nagaji physiology varies somewhat. Some possess longer necks than others, some sport impressive fangs that can inject venom, and some are so unique they resemble lamias more than their own nagaji kin. Like snakes, nagaji are cold-blooded and shed their skin periodically; as a result, nagaji territories rarely overlap with those of mammalian humanoids, since their environmental needs diverge so widely. They're best known for their crushing, snakelike strength, but their close ties to nagas mean many nagaji have the potential for powerful magic as well.

Long ago, the naga goddess Nalinivati created the first nagaji as the backbone of a society that respected nagas. But the nagaji were never mindless vassals, and the goddess gifted them with free will. Many nagaji willingly serve nagas to this day, honoring some as outright divinities. While outsiders might regard nagaji initially as brainwashed servants, nagaji dispute this claim. Of course there are evil and unfair naga overlords, but there are just as many fair and just naga rulers, and nagaji history remembers various rebellions and revolutions to support a new naga's claims of rulership when a matriarch overstepped her bounds. Nagaji accurately note that their long history with nagas is no simple matter and claim that the partnership goes both ways: nagas rely as much on nagaji for the running of their empires as nagaji rely on nagas to lead their people to prosperity.

Although nagaji might be encountered in diverse cities and urban centers, their communities are concentrated in environments that suit their biology, namely jungles and tropical forests. Where many species would languish in the heat and humidity, nagaji bask in the warmth and thrive.

```statblock
creature: "Nagaji Soldier"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
