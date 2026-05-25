---
type: creature
group: ["Fey", "Fire"]
statblock: true
layout: Basic Pathfinder 2e Layout
name: "Elananx"
level: "6"
rare_01: "Common"
rare_02: ""
rare_03: ""
rare_04: ""
alignment: ""
size: "Medium"
trait_01: "Fey"
trait_02: "Fire"
trait_03: ""
trait_04: ""
trait_05: ""
trait_06: ""
trait_07: ""
perception:
  - name: Perception
    desc: "+14; [[Darkvision]]"
languages: "Fey ((Can't Speak Any Language))"
skills:
  - name: Skills
    desc: "Acrobatics +14, Athletics +14, Survival +14"
abilityMods: ["+4", "+4", "+2", "-3", "+2", "-2"]
abilities_top:
  - name: "Pack Attack"
    desc: "The elananx's Strikes deal an extra 1d6 damage to creatures within the reach of at least two of its allies."
armorclass:
  - name: AC
    desc: "24; **Fort** +12, **Ref** +16, **Will** +12"
health:
  - name: HP
    desc: "95; **Immunities** fire; **Weaknesses** cold iron 5"
abilities_mid:
  - name: "Cinder Dispersal"
    desc: "`pf2:r` **Frequency** once per day <br>  <br> **Trigger** The elananx takes damage from a hostile source <br>  <br> **Effect** The elananx disperses into a cloud of smoke and cinders, filling its space and a @Template[emanation|distance:20]. While in this form, the elananx can't be attacked or targeted, and it doesn't take up space. Anything inside this cloud is [[Concealed]], and any creature ending its turn there takes @Damage[2d6[fire]|options:area-damage] damage. At the start of its turn, the elananx returns to its normal form in any square the cloud covered. If the elananx Strikes a creature using its first action after returning to its normal form, the target is [[Off Guard]] and the Strike deals an extra 1d6 fire damage."
speed: "0 feet"
attacks:
  - name: "Melee strike"
    desc: "Jaws +16 (`pf2:1`) (magical, unarmed), **Damage** 2d6+8 piercing plus 1d6 fire"
  - name: "Melee strike"
    desc: "Claw +16 (`pf2:1`) (agile, unarmed), **Damage** 2d6+8 slashing"
spellcasting: []
abilities_bot:
  - name: "Pounce"
    desc: "`pf2:1` The elananx Strides and makes a Strike at the end of that movement. If the elananx began this action [[Hidden]], it remains hidden until after the attack."
sourcebook: "Monster Core"
source-type: "Remaster"
---
### `= this.file.name`

These strange, fey felines resemble large, broad bobcats from a distance, but a closer view reveals something amiss. Their forms ripple and billow with heat, and their eyes glow from within as if they contained tiny, flickering flames. The pungent scent of rotting leaves smoldering in a bonfire clings to their fur. Yet those who have the chance to watch elananxes hunt or attack prey witness the greatest indication that these creatures are something more than mere predators, for they act with cruel and savvy instincts, reveling in the pain they inflict.

Elananxes typically hunt alone, but sometimes these cunning and malicious hunters of the First World roam in packs called billows to take down large prey. Like many house cats, elananxes are not content to merely track and devour prey, but prefer to toy with their victims, drawing joy from the fear and pain of those they capture. To this end, elananxes rarely use their cinder dispersal ability to evade their targets, instead opting to foil their quarry just before the end of the hunt—though, as selfish creatures who wish to live to hunt again, elananxes often reserve one use of this ability, just in case.

Because of their clever and malicious ways, elananxes are favored as hunting companions by redcaps, who go out of their way to befriend or make deals with these creatures. Redcaps also find great sport in hunts where competing elananxes chase a single creature. Although they're large enough to serve as mounts for redcaps, elananxes despise being ridden and resist such attempts—little is as sure to cause a supposedly friendly elananx to turn on its redcap ally as a foolhardy attempt to treat the fey cat as a horse!

Elananxes have a strange affinity with forest fires. Because they are immune to the damage caused by flickering flames, they enjoy capering and caterwauling through the smoky, burning ruins of forest infernos. Some have even been known to use their burning bites to deliberately light undergrowth on fire, simply so they might experience the beauty of the flames combined with the inevitable pain such disasters inflict on other creatures.

```statblock
creature: "Elananx"
```

**Source:** `= this.sourcebook` (`= this.source-type`)
